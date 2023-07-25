from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Shoping_cart
from django.http import HttpResponse, HttpResponseNotFound, Http404
from product.models import *
from django.db.models import Prefetch, Q, F
from django.contrib.auth.decorators import login_required



@login_required
def basket_view(request):
    baskets = Shoping_cart.objects.select_related('id_product').filter(id_user=request.user)
    context = {
        'products': baskets,
    }
    return render(request, 'basket/cart.html', context)
 
 
   
@login_required 
def basket_add(request, product_id):
    current = request.META.get('HTTP_REFERER')
    
    product = Product.objects.get(id=product_id)
    baskets = Shoping_cart.objects.filter(id_user=request.user, id_product=product)
    
    if not baskets.exists():
        basket = Shoping_cart(id_user=request.user, id_product=product)
        basket.save()
        return HttpResponseRedirect(current)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current)
       
 
@login_required      
def basket_delete(request, product_id):
    basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user))
    
    # if (basket.quantity == 1):
    basket.delete()
    # else:
    #     basket.update(quantity=Q('quantity') - 1)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    
@login_required    
def basket_increment_count(request, product_id):
    basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user)).select_related('id_product')
    if basket[0].quantity < basket[0].id_product.count:
        basket.update(quantity=F('quantity') + 1)
    else:
        # error
        pass
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required   
def basket_decrement_count(request, product_id):
    basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user)).select_related('id_product')
    
    if (basket[0].quantity == 1):
        basket.delete()
    else:
        basket.update(quantity=F('quantity') - 1)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
    

        