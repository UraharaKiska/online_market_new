
from django.contrib import admin
from django.urls import path, include
from .views import *
from users.views import *


urlpatterns = [
    path('', Content, name="home"),
    path('contact', ContactUs, name="contact"),
    path('about', AboutPage, name="about"),
    path('login', LoginUser.as_view(), name="login"),
    path('register', RegisterUser.as_view(), name="register"),

]
