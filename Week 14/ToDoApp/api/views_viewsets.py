import logging

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.db.models import Avg, Max, Min, Sum, Count
from .serializers import TaskListModelSerializer, MyUserSerializer
from .models import TaskList, MyUser

logger = logging.getLogger(__name__)


class TaskListListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListModelSerializer

    def get_queryset(self):
        if self.action == 'list':
            return TaskList.objects.select_related('created_by')
        return TaskList.objects.all()

    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'TaskList object created, name: {serializer.instance.name}')
        logger.info(f'TaskList object created, name: {serializer.instance.name}')
        logger.warning(f'TaskList object created, name: {serializer.instance.name}')
        logger.error(f'TaskList object created, name: {serializer.instance.name}')
        logger.critical(f'TaskList object created, name: {serializer.instance.name}')


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    # queryset = MyUser.objects.annotate(tasklists_count=Count('tasklists'))
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_queryset(self):
        if self.action == 'list':
            return MyUser.objects.prefetch_related('tasklists')
        return MyUser.objects.all()


