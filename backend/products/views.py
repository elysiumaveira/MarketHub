from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Product
from .serializer import ProductSerializer


class ProductReadView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
