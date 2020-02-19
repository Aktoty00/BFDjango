from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import task_list, task_lists_num

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('task_lists/', task_list),
    path('task_lists/<int:pk>/', task_lists_num),
]