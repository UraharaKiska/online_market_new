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
from django.views.decorators.http import require_POST
from .cart import Cart
import copy

# @login_required
def basket_view(request):
    
    if request.user.is_authenticated:
        baskets = Shoping_cart.objects.filter(id_user=request.user).order_by("-date_create").select_related('id_product')
    
        context = {
            'products': baskets,
        }
    else:
        cart = Cart(request)

        context = {'products': cart}
        # cart = request.session.get('cart')
        for c in cart:
            print(c)
        
    return render(request, 'basket/cart.html', context)
 
 
def basket_add_mixin(request, product, quantity=1):
        baskets = Shoping_cart.objects.filter(id_user=request.user, id_product=product)
        if not baskets.exists():
            basket = Shoping_cart(id_user=request.user, id_product=product)
            basket.save()
        else:
            basket = baskets.first()
            basket.quantity += quantity
            basket.save()



# @login_required 
# @require_POST
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    current = request.META.get('HTTP_REFERER')

    if request.user.is_authenticated:
       basket_add_mixin(request, product)
        
    else:
        cart = Cart(request)                # session
        cart.add(product=product)
       
        
    return HttpResponseRedirect(current)



       
 
# @login_required 
# @require_POST     
def basket_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user))
        # if (basket.quantity == 1):
        basket.delete()
        # else:
        #     basket.update(quantity=Q('quantity') - 1)
    else:
        cart = Cart(request)
        cart.remove(product)


            
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    
# @login_required 
# @require_POST   
def basket_increment_count(request, product_id):
    if request.user.is_authenticated:
        basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user)).select_related('id_product')
        if basket[0].quantity < basket[0].id_product.count:
            basket.update(quantity=F('quantity') + 1)
        else:
            # error
            pass
    else:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required  
# @require_POST   
def basket_decrement_count(request, product_id):
    if request.user.is_authenticated:
        basket = Shoping_cart.objects.filter(Q(id_product=product_id) & Q(id_user=request.user)).select_related('id_product')
        
        if (basket[0].quantity == 1):
            basket.delete()
        else:
            basket.update(quantity=F('quantity') - 1)
    else:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity = -1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
    

def basket_add_session(request, cart):
    for c in cart:
        print(c)
        product=c['product']
        basket_add_mixin(request, product, quantity=c['quantity'])
    
