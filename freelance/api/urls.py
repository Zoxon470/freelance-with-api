from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = router.urls