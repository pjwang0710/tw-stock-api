from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaiwanStockInfoSerializer
from .models import TaiwanStockInfo
from users.models import UserSecretKeys
from users.serializers import UserSecretKeySerializer
import uuid
import datetime


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_stock_info(request, pk, secret_key):
    user_secret = UserSecretKeys.objects.get(secret_key=secret_key, is_valid=True)
    count = user_secret.count + 1
    serializer = UserSecretKeySerializer(instance=user_secret, data={'count': count}, partial=True)
    if serializer.is_valid():
        serializer.save()
    stock_infos = TaiwanStockInfo.objects.filter(stock_id=pk)
    serializer = TaiwanStockInfoSerializer(stock_infos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_api_user_count(request, pk):
    user_secret = UserSecretKeys.objects.get(user_id=pk, is_valid=True)
    serializer = UserSecretKeySerializer(user_secret, many=False)
    return Response(serializer.data)
