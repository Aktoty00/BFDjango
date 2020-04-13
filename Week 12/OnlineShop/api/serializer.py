from rest_framework import serializers
from .models import CategoryList, ProductList, MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = MyUserSerializer(read_only=True)
    desc = serializers.CharField()
    photo = serializers.ImageField()
    document = serializers.FileField()

    def create(self, validated_data):
        category = CategoryList(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = ProductList
        fields = '__all__'
