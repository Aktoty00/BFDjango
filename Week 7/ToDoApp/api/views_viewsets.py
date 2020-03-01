from rest_framework import viewsets
from rest_framework import mixins
from .serializers import TaskListSerializer, MyUserSerializer
from .models import TaskList, MyUser


class TaskListListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
