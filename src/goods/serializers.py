from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Product, Category


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('slug', 'name', 'image', 'price')


class CategorySerializer(ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = '__all__'
