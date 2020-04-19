from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from api.models import CategoryList, ProductList
from api.serializer import CategoryListSerializer, ProductListSerializer


class CategoryListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            generics.GenericAPIView):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductsAPIView(generics.ListCreateAPIView, generics.CreateAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        try:
            category = CategoryList.objects.get(id=self.kwargs.get('pk'))
        except CategoryList.DoesNotExist:
            raise Http404
        queryset = category.products.all()
        return queryset
