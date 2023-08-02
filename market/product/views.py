from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404
from reviews.models import *
# Create your views here.


def Content(request):
    return render(request, 'product/content.html')

def ContactUs(request):
    return render(request, 'product/contact.html')

def AboutPage(request):
    return render(request, 'product/content.html')



# class ShowProduct(DetailView):
#     model = Product
#     template_name = 'product/card.html'
#     slug_url_kwarg = 'product_slug'
#     context_object_name = 'product'

#     def get_queryset(self):
#         return ProductPhoto.objects.select_related('id_product').filter(id_product.slug=True)
    



class ProductListShow(ListView):
    paginate_by = 4
    model = Product
    template_name = 'product/content.html'
    context_object_name = "products"

    
    def get_queryset(self):
        return ProductPhoto.objects.select_related('id_product').order_by('-id_product__id', 'id_product__date_create').distinct('id_product')
    
   
class ProductType(ListView):
    paginate_by = 4
    model = Product_type
    template_name = "product/content.html"
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(product__slug=self.kwargs['product_type_slug'], available=True).select_related('product_type')



def show_product(request, product_slug):
    product = ProductPhoto.objects.select_related('id_product').filter(id_product__slug = product_slug)
    if len(product) == 0:
        raise Http404
    
    reviews = Reviews.objects.filter(product=product[0].id_product)
    reviews_count = len(reviews)
    rating = 0.0
    for r in reviews:
        rating += r.rating
        r.rating = list(i for i in range(0, r.rating))
        print(r.rating)
    if rating:
        rating = round(float(rating) / reviews_count, 1)

    
    
    context = {
        'product': product,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'rating': rating,
    }
    
    return render(request, 'product/card.html', context)