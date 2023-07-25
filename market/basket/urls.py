from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', basket_view, name="basket"),
    path('basket-add/<int:product_id>/', basket_add, name="basket_add"),
    path('basket-delete/<int:product_id>/', basket_delete, name="basket_delete"),
    path('increment-count/<int:product_id>/', basket_increment_count, name="increment"),
    path('decrement-count/<int:product_id>/', basket_decrement_count, name="decrement"),
    
    
]