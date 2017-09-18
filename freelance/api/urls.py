from django.conf.urls import url, include
from rest_framework import routers
from api.views import ExecutorViewSet, CustomerViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'executor', ExecutorViewSet, base_name='executor')
router.register(r'customers', CustomerViewSet, base_name='customers')
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = router.urls