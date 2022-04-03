from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from products_api.models import Product, Category
from products_api.serializers import ProductSerializer, CategorySerializer
from profiles_api.models import UserProfile


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        res = Category.objects.filter(id=params['pk'])
        serializer = CategorySerializer(res, context={"request": request}, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        product_data = request.data
        priceInt = int(float(product_data['price']))
        stockInt = int(float(product_data['stock']))
        new_product = Product.objects.create(
            name=product_data['name'],
            description=product_data['description'],
            image1=product_data['image1'],
            image2=product_data['image2'],
            image3=product_data['image3'],
            price=priceInt,
            stock=stockInt,
            user=UserProfile.objects.get(id=product_data['user']),
        )
        new_product.save()
        serializer = ProductSerializer(new_product)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        res = Product.objects.filter(id=params['pk'])
        # res = Category.objects.get(id=params['pk'])

        serializer = ProductSerializer(res, context={"request": request}, many=True)
        return Response(serializer.data)

