from rest_framework.generics import (ListAPIView, CreateAPIView)

from .models import MainCategory, SubCategory
from .serializer import MainCategorySerializer, SubCategorySerializer


class MainCategoryReadView(ListAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class MainCategoryCreateView(CreateAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class SubCategoryReadView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryCreateView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
