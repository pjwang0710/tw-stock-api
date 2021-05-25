from rest_framework import serializers
from .models import TaiwanStockInfo


class TaiwanStockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockInfo
        fields = '__all__'
