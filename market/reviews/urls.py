
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', show_all_reviews, name='all_review'),
    path('<slug:product_slug>', leave_review, name='leave_review'),
    
]

