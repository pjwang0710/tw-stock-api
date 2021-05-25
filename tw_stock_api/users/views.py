from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserSecretKeySerializer
from .models import Users, UserSecretKeys
import uuid
import datetime


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


@api_view(['POST'])
def login(request):
    user = Users.objects.filter(email=request.data.get('email'), hashed_password=request.data.get('hashed_password'))
    if user:
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    return Response({'failed'}, status=status.HTTP_400_BAD_REQUEST)


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
