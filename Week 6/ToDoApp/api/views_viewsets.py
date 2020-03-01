from rest_framework import viewsets
from rest_framework import mixins
from .serializers import TaskListSerializer
from .models import TaskList


class TaskListListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
