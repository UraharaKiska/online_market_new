
from django.contrib import admin
from django.urls import path, include
from market import settings
from django.conf.urls.static import static
from basket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('basket.urls')),   
    path('', include('product.urls')),
    path('users/', include('users.urls')),
    
    

]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls"))
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

