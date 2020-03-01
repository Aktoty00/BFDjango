from rest_framework import serializers
from .models import CategoryList, ProductList


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'
