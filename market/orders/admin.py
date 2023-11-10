from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = Orders_Item
    raw_id_fields = ['product']


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 
                    'postal_code', 'city', 'paid', 
                    'date_create', 'date_update']
    list_filter = ['paid', 'date_create', 'date_update']
    inlines = [OrderItemInline]

admin.site.register(Order_status)

