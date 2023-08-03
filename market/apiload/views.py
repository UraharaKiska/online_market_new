from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
# Create your views here.


class ProductAPIList(APIView):
    
    def get(self, request):
        product = Product.objects.filter(available=True)
        serializer = ProductListSerializer(product, many=True)
        return Response(serializer.data)
    
    

class ReviewAPIList(APIView):
    
    def get(self, request, product_slug):
        reviews = Reviews.objects.filter(product__slug=product_slug)
        serializer = ReviewsListSerializer(reviews, many=True)
        return Response(serializer.data)