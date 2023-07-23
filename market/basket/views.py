from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404



def basket_view(request):
    return render(request, 'basket/cart.html')
   