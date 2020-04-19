from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views_viewsets import TaskListListViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task_lists', TaskListListViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
urlpatterns.append(path('login/', obtain_jwt_token))
