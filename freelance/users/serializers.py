from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'is_superuser', 'user_type')


class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')