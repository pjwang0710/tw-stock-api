from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserSecretKeySerializer
from .models import Users, UserSecretKeys
import uuid
import datetime
from dateutil.relativedelta import relativedelta
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from pydantic import BaseModel
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Optional
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend
from django.db.models import Sum


class UserObj(BaseModel):
    id: str
    email: str
    token: Optional[str] = None


class ExampleAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
            user = Users.objects.filter(id=valid_data.get('user_id')).first()
        except Exception:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((ExampleAuthentication, ))
def get_user_detail(request):
    user_id = request.user.id
    user = Users.objects.all().filter(id=user_id)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='123@123'),
        'hashed_password': openapi.Schema(type=openapi.TYPE_STRING, description='123'),
    }
))
@api_view(['POST'])
def login(request):
    user = Users.objects.filter(email=request.data.get('email'), hashed_password=request.data.get('hashed_password'))
    if user:
        serializer = UserSerializer(user, many=True)
        user_obj = UserObj(**dict(serializer.data[0]))
        tokens = get_tokens_for_user(user_obj)
        user_obj.token = tokens.get('access')
        return Response(dict(user_obj))
    return Response({'failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((ExampleAuthentication, ))
def test_jwt(request):
    return Response({'userId': request.user.id}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='post',
                     responses={
                         '200': openapi.Response('response description', UserSerializer)
                     },
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         properties={
                             'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='email'),
                             'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='first name'),
                             'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='last name'),
                             'hashed_password': openapi.Schema(type=openapi.TYPE_STRING, description='hashed_password'),
                         }
                     )
                    )
@api_view(['POST'])
def insert_user(request):
    user = Users.objects.filter(email=request.data.get('email'))
    if user:
        return Response({'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes((ExampleAuthentication, ))
def update_user(request):
    user_id = request.user.id
    user = Users.objects.get(id=user_id)
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = Users.objects.get(id=pk)
    user.delete()
    return Response('Delete successfully!')


@api_view(['GET'])
@authentication_classes((ExampleAuthentication, ))
def get_secret_key_detail(request):
    user_id = request.user.id
    print('user id', user_id)
    obj = UserSecretKeys.objects.all().filter(user_id=user_id, is_valid=1)
    if obj:
        serializer = UserSecretKeySerializer(obj, many=True)
        return Response(serializer.data)
    return Response({'status': 'failed'})


@api_view(['POST'])
@authentication_classes((ExampleAuthentication, ))
def update_user_secret(request):
    user_id = request.user.id
    user = Users.objects.get(id=user_id)
    if user:
        secret_keys = UserSecretKeys.objects.all().filter(user_id=user_id)
        instances = []
        for obj in secret_keys:
            obj.is_valid = False
            obj.save()
            instances.append(obj)
        serializer = UserSecretKeySerializer(instances, many=True)

        now = datetime.datetime.utcnow()
        data = {
            'user': user_id,
            'secret_key': str(uuid.uuid4()).replace('-', ''),
            'created_at': now,
            'year': now.year,
            'month': now.month,
            'count': 0,
            'is_valid': True,
            'is_charged': False
        }
        serializer = UserSecretKeySerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response({'status': 'failed'})


@api_view(['GET'])
@authentication_classes((ExampleAuthentication, ))
def get_api_use_count(request):
    user_id = request.user.id
    mapping = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'Mar',
        '4': 'Apr',
        '5': 'May',
        '6': 'Jun',
        '7': 'Jul',
        '8': 'Aug',
        '9': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec'
    }
    user = Users.objects.get(id=user_id)
    now = datetime.datetime.utcnow()
    mock_data = {}
    for i in range(6, -1, -1):
        year = (now - relativedelta(months=i)).year
        month = (now - relativedelta(months=i)).month
        mock_data[f'{year}_{month}'] = 0
    output_labels = []
    output_data = []
    if user:
        data = UserSecretKeys.objects.filter(user_id=user_id).values('user_id', 'year', 'month').annotate(total_count=Sum('count'))
        for sub_data in data:
            key = f'{sub_data["year"]}_{sub_data["month"]}'
            if mock_data.get(key, None) is not None:
                mock_data[key] = sub_data['total_count']
        for year_month_key in mock_data.keys():
            output_labels.append(mapping[year_month_key.split('_')[1]])
            output_data.append(mock_data[year_month_key])
        return Response({
            'labels': output_labels,
            'data': output_data
        })
    return Response({'status': 'failed'})
