from rest_framework.generics import ListAPIView

from models import Category, Product


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer
