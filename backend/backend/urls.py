from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

from categories.views import (
    MainCategoryReadView, 
    MainCategoryCreateView,
    SubCategoryReadView,
    SubCategoryCreateView,
)

from products.views import (
    ProductReadView,
    ProductCreateView,
)


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    #Categories
    path('main-categories/', MainCategoryReadView.as_view(), name='Main categories'),
    path('main-category-create/', MainCategoryCreateView.as_view(), name='Create main category'),
    path('sub-categories/', SubCategoryReadView.as_view(), name='Sub categories'),
    path('sub-category-create/', SubCategoryCreateView.as_view(), name='Create sub category'),

    #Products
    path('products/', ProductReadView.as_view(), name='Products'),
    path('create-product/', ProductCreateView.as_view(), name='Create product'),

    #Authentication system
    path('api/users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
