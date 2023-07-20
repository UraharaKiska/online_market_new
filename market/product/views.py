from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Content(request):
    return render(request, 'product/content.html')

def ContactUs(request):
    return render(request, 'product/contact.html')

def AboutPage(request):
    return render(request, 'product/content.html')

