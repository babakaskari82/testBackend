from django.urls import path, include
from products_api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('products', views.ProductView, basename='products')
router.register('categories', views.ProductView, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
