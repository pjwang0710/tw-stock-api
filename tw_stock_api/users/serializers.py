from rest_framework import serializers
from .models import Users, UserSecretKeys


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
