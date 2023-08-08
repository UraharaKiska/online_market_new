from rest_framework import serializers
from product.models import *
from reviews.models import *


class ReviewsListSerializer(serializers.ModelSerializer):

    product = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    
    product_type = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reviews = ReviewsListSerializer(many=True)
    rating = serializers.SlugRelatedField(slug_field="rating", read_only=True)
    
    
    class Meta:
        model = Product
        # fields = ['name', 'slug', 'old_price', 'new_price', 'count', 'product_type', 'rating]
        exclude = ("available", )
        
        
