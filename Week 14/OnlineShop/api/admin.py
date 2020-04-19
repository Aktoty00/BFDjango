from django.contrib import admin

from api.models import MyUser, CategoryList, ProductList, Profile


@admin.register(CategoryList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(ProductList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'address',)
