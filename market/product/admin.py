from django.contrib import admin
from users.models import *
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'new_price', 'count', 'available')
    prepopulated_fields = {"slug": ("name",)}


class Product_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(CustomUser)
admin.site.register(Product_type, Product_typeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto)




