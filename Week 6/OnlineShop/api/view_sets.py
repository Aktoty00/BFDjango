from rest_framework import mixins, viewsets

from api.models import CategoryList, ProductList
from api.serializer import CategoryListSerializer, ProductListSerializer


class CategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer


class ProductListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
