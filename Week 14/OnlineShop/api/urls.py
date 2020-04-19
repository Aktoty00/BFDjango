from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from api.view_sets import CategoryListViewSet, ProductListViewSet, UserViewSet
from .views import CategoryListAPIView, CategoryDetailAPIView, ProductsAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', CategoryListViewSet)
router.register(r'product', ProductListViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('category/<int:pk>/products/', ProductsAPIView.as_view()),
] + router.urls
