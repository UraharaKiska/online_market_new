from django.shortcuts import render, redirect, reverse

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from .models import *
from django.http import Http404, HttpResponseRedirect


@login_required
def show_all_reviews(request):
    return render(request, 'reviews/show_all.html')

@login_required
def leave_review(request, product_slug):
    product_name = ""
    if (request.POST):
        rating = request.POST['rating']
        comment = request.POST['comment']
        product = Product.objects.get(slug=product_slug)
        try:
            query = Reviews.objects.create(product=product, user=request.user, rating=rating, comment=comment)
        except Exception as ex:
            
            raise Http404(ex)
        return redirect('orders')
        
    else:
        review = Reviews.objects.filter(user=request.user, product__slug=product_slug)
        if (review):
            raise Http404('Already exist')
        product_name = Product.objects.filter(slug=product_slug).values('name').first()
    
    context ={
        'product_name': product_name,
    }
    
    
    return render(request, 'reviews/leave_review.html', context)
    


