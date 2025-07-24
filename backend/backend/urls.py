from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from categories.views import (
    MainCategoryReadView, 
    MainCategoryCreateView,
    SubCategoryReadView,
    SubCategoryCreateView,
)


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    #Categories
    path('main-categories/', MainCategoryReadView.as_view(), name='Main categories'),
    path('main-category-create/', MainCategoryCreateView.as_view(), name='Create main category'),
    path('sub-categories/', SubCategoryReadView.as_view(), name='Sub categories'),
    path('sub-category-create/', SubCategoryCreateView.as_view(), name='Create sub category'),
]
