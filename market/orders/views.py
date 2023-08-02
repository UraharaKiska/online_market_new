from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import  F
from product.models import ProductPhoto, Product
from .models import *
from basket.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
# Create your views here.
hui = {}
# for ord in orders:
#     products[ord.full_order_id] = Orders_inform.objects.filter(full_order=ord.full_order_id).select_related('product')
#     hui[ord.full_order_id] = []
#     for i in range(0, len(products[ord.full_order_id])):
#         hui[ord.full_order_id].append(products[ord.full_order_id][i].product)


@login_required      
def orders_list_show(request):
    orders = Orders_data.objects.filter(user__username=request.user)
    products = {}
    for ord in orders:
        prod = Orders_inform.objects.filter(full_order=ord.full_order_id).select_related('product')
        products[ord.full_order_id] = {}

        for i in prod:
            p = ProductPhoto.objects.filter(id_product=i.product).select_related('id_product').first()
            products[ord.full_order_id][i.product] = {}
            products[ord.full_order_id][i.product]['img'] = p.photo
            products[ord.full_order_id][i.product]['slug'] = p.id_product.slug
            
  

    context = {
        'orders': orders,
        'products': products,
    }

    # print(products)


    return render(request, 'orders/orders-list.html', context)



@login_required      
def do_order(request):
    basket = Shoping_cart.objects.filter(id_user=request.user).values('id_product__name', 'quantity', 'id_product__old_price', 'id_product__new_price')
    photo = {}
    total_price = 0
    for key in basket:
        photo[key['id_product__name']] = ProductPhoto.objects.filter(id_product__name=key['id_product__name']).first().photo
        if key['id_product__new_price']:
            total_price += key['id_product__new_price'] *  key['quantity']
        else:
            total_price += key['id_product__old_price'] *  key['quantity']
            
         
    
    context = {
        'products': basket,
        'photo': photo,
        'total_price': total_price,
        
    }
    
    # print(photo)
    return render(request, 'orders/do-order.html', context)


@login_required      
def confirm_order(request):
    
    basket = Shoping_cart.objects.filter(id_user=request.user).select_related('id_product')
    order = Orders_data(user=request.user)
    order.save()
    full_order = Orders_data.objects.filter(user=request.user).last().full_order_id
    for b in basket:
        add = Orders_inform(product=b.id_product, count=b.quantity, full_order_id=full_order)
        add.save()
        product = Product.objects.filter(id=b.id_product.id).update(count=F('count') - b.quantity)
        
    
    basket.delete()
    messages.success(request, 'Order successfully confirmed')
    return redirect('home')
 
    
@login_required          
def my_order_show(request, order_slug):
    order = Orders_data.objects.filter(full_order_id=order_slug).first()
    if order is None or order.user != request.user:
        raise Http404('Order not found')
    products = {}
    prod = Orders_inform.objects.filter(full_order=order.full_order_id).select_related('product')
    
    for i in prod:
        p = ProductPhoto.objects.filter(id_product=i.product).select_related('id_product').first()
        products[i.product] = {}
        products[i.product]['img'] = p.photo
        products[i.product]['price'] = i.price_for_one
        products[i.product]['count'] = i.count
        
        

    
    total_price = order.total_price
    order_status = order.status
    
        
    context = {
        'products': products,
        'total_price': total_price,
        'order_status': order_status,
    }
         
    print(products)
    print(total_price)

    return render(request, 'orders/my_order.html', context)
        