from rest_framework import serializers
from users.models import User
from task.models import Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'user_type', 'balance')


class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'money', 'assignee', 'created_by')

    def get_assignee(self, obj):
        return {
            'id': obj.assignee.id,
            'username': obj.assignee.username,
            'first_name': obj.assignee.first_name,
            'last_name': obj.assignee.last_name,
            'user_type': obj.assignee.user_type,
            'balance': obj.assignee.balance
        }

    def get_created_by(self, obj):
        return {
            'id': obj.created_by.id,
            'username': obj.created_by.username,
            'first_name': obj.created_by.first_name,
            'last_name': obj.created_by.last_name,
            'user_type': obj.created_by.user_type,
            'balance': obj.created_by.balance,
        }




