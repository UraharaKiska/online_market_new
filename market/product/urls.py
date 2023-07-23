
from django.contrib import admin
from django.urls import path, include
from .views import *
from users.views import *

urlpatterns = [
    path('', ProductListShow.as_view(), name="home"),
    path('contact', ContactUs, name="contact"),
    path('about', AboutPage, name="about"),
    path('login', LoginUser.as_view(), name="login"),
    path('register', RegisterUser.as_view(), name="register"),
    path('logout', logout_user, name="logout"),
    path('<slug:product_slug>/', show_product, name='product'),
    path('product_type/<slug:product_type_slug>', ProductType.as_view(), name='product_type'),
    
    
]

