from django.contrib import admin
from django.urls import path, include
from .views import *

# app_name = "product"

urlpatterns = [
    path('my_orders', orders_list_show, name="orders"),
    path('order', do_order, name="do-order"),
    path('confirm-order', confirm_order, name="confirm-order"),
    path('my_orders/<slug:order_slug>', my_order_show, name="my_order"),
    
    
    # path('<slug:full_order_id', order_show, name="order-page"),
    
    
]
