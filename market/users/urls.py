
from django.urls import path, include
from .views import *


urlpatterns = [
    
    path('login', LoginUser.as_view(), name="login"),
    path('register', RegisterUser.as_view(), name="register"),
    path('logout', logout_user, name="logout"),
    path('lk', profile_update, name="lk"),

]