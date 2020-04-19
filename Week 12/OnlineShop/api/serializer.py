from rest_framework import serializers
from .models import CategoryList, ProductList, MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')


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


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = MyUserSerializer(read_only=True)
    desc = serializers.CharField()
    photo = serializers.ImageField()
    document = serializers.FileField()
    products = ProductListSerializer(many=True, required=False)

    def create(self, validated_data):
        # products = validated_data.pop('products')
        category = CategoryList.objects.create(**validated_data)
        # for product in products:
        #     ProductList.objects.create(category=category, **product)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
