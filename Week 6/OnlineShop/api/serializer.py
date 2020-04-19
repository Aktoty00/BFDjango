from rest_framework import serializers
from .models import CategoryList, ProductList


class CategoryListSerializer1(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer1(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProductList
        fields = ('id', 'name', 'price', 'category', 'category_id')


class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, required=False)

    class Meta:
        model = CategoryList
        fields = ('id', 'name', 'products')

    def create(self, validated_data):
        # products = validated_data.pop('product')
        category = CategoryList.objects.create(**validated_data)
        # for product in products:
        #     ProductList.objects.create(category=category, **product)
        return category
