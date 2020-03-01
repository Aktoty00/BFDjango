from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    pass


class CategoryList(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'CategoryList'
        verbose_name_plural = 'CategoryLists'

    def __str__(self):
        return 'Category name: {}'.format(self.name)


class ProductList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    category = models.ForeignKey(CategoryList, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'ProductList'
        verbose_name_plural = 'ProductLists'

    def __str__(self):
        return 'Product name: {}'.format(self.name)

