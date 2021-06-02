from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserSecretKeySerializer
from .models import Users, UserSecretKeys
import uuid
import datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from pydantic import BaseModel
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Optional
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend


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
def get_user_detail(request, pk):
    user = Users.objects.all().filter(id=pk)
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
    print(request.user.id)
    return Response({'True'}, status=status.HTTP_200_OK)



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
def update_user(request, pk):
    user = Users.objects.get(id=pk)
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
def get_secret_key_detail(request, pk):
    obj = UserSecretKeys.objects.all().filter(user_id=pk, is_valid=1)
    if obj:
        serializer = UserSecretKeySerializer(obj, many=True)
        return Response(serializer.data)
    return Response({'status': 'failed'})


@api_view(['POST'])
def update_user_secret(request, pk):
    user = Users.objects.get(id=pk)
    if user:
        secret_keys = UserSecretKeys.objects.all().filter(user_id=pk)
        instances = []
        for obj in secret_keys:
            obj.is_valid = False
            obj.save()
            instances.append(obj)
        serializer = UserSecretKeySerializer(instances, many=True)

        now = datetime.datetime.utcnow()
        data = {
            'user': pk,
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
