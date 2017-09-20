from rest_framework import viewsets


from users.models import User
from task.models import Task
from .serializers import UserSerializer, TaskSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(user_type=User.EXECUTOR)
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().filter(user_type=User.CUSTOMER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



