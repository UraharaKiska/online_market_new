

from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('product', ProductAPIList.as_view(), name="product-api"),
    path('review/<slug:product_slug>', ReviewAPIList.as_view(), name="product-api"),
    
    # re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    

]
