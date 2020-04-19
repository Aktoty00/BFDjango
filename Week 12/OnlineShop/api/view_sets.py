import logging

from rest_framework import mixins, viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .models import CategoryList, ProductList, MyUser
from .serializer import CategoryListSerializer, ProductListSerializer, MyUserSerializer

logger = logging.getLogger(__name__)


class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Category object created, name: {serializer.instance.name}')
        logger.info(f'Category object created, name: {serializer.instance.name}')
        logger.warning(f'Category object created, name: {serializer.instance.name}')
        logger.error(f'Category object created, name: {serializer.instance.name}')
        logger.critical(f'Category object created, name: {serializer.instance.name}')


class ProductListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Product object created, name: {serializer.instance.name}')
        logger.info(f'Product object created, name: {serializer.instance.name}')
        logger.warning(f'Product object created, name: {serializer.instance.name}')
        logger.error(f'Product object created, name: {serializer.instance.name}')
        logger.critical(f'Product object created, name: {serializer.instance.name}')


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
