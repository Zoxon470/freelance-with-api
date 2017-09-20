from rest_framework import serializers
from users.models import User
from task.models import Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'user_type', 'balance')


class TaskSerializer(serializers.ModelSerializer):
    assignee_info = UserSerializer(read_only=True, source='assignee')
    assignee = serializers.IntegerField(allow_null=True, source='assignee_id')
    created_by_info = UserSerializer(read_only=True, source='created_by')
    created_by = serializers.IntegerField(allow_null=True, source='created_by_id')

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'cost', 'assignee', 'assignee_info', 'created_by', 'created_by_info',)


