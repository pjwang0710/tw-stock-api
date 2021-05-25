from rest_framework import serializers
from .models import Users, UserSecretKeys


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSecretKeySerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = UserSecretKeys
        fields = '__all__'
