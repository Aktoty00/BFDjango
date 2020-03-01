from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views_viewsets import TaskListListViewSet
from .views import TaskListListAPIView, TaskListDetailAPIView

# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('task_lists/', TaskListListAPIView.as_view()),
#     path('task_lists/<int:pk>/', TaskListDetailAPIView.as_view()),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'task_lists', TaskListListViewSet)

urlpatterns = router.urls
