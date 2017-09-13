from rest_framework import serializers
from users.models import User
from task.models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user_detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'is_superuser', 'user_type')



# class TaskSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="task_detail")
#
#     class Meta:
#         model = Task
#         fields = ('id', 'url', 'title', 'description', 'money', 'assignee', 'created_by')