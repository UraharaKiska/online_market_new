
from django.contrib import admin
from django.urls import path, include, re_path
from market import settings
from django.conf.urls.static import static
from basket import views

urlpatterns = [
    path('reviews/', include('reviews.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('basket.urls')),   
    path('', include('product.urls')),
    path('users/', include('users.urls')),
    
    
    # re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    

]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls"))
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

