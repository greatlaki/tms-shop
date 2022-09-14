from rest_framework.generics import ListAPIView

from models import Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
