from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskListSerializer
from .models import TaskList


class TaskListListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskListDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
