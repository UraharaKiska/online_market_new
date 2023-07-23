from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
# Create your views here.


def Content(request):
    return render(request, 'product/content.html')

def ContactUs(request):
    return render(request, 'product/contact.html')

def AboutPage(request):
    return render(request, 'product/content.html')



class ShowProduct(DeleteView):
    template_name = 'product/content.html'


class ProductListShow(ListView):
    paginate_by = 5
    model = Product
    template_name = 'product/content.html'
    context_object_name = "products"
    
    
    def get_queryset(self):
        return ProductPhoto.objects.select_related('id_product').distinct('id_product')
    
    
class ProductType(ListView):
    paginate_by = 5
    model = Product_type
    template_name = "product/content.html"
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(product__slug=self.kwargs['product_type_slug'], available=True).select_related('product_type')

