from rest_framework import mixins, viewsets

from .models import CategoryList, ProductList, MyUser
from .serializer import CategoryListSerializer, ProductListSerializer, MyUserSerializer


class CategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer


class ProductListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
