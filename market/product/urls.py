
from django.contrib import admin
from django.urls import path, include
from .views import *
from users.views import *
from basket.views import *

# app_name = "product"

urlpatterns = [
    path('', ProductListShow.as_view(), name="home"),
    path('contact', ContactUs, name="contact"),
    path('about', AboutPage, name="about"),
    path('<slug:product_slug>/', show_product, name='product'),
    path('product_type/<slug:product_type_slug>', ProductType.as_view(), name='product_type'),
    
    
    
]

