from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user_detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'is_superuser', 'user_type')
