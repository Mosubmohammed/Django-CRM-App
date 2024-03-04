from .views import *
from django.urls import path 
urlpatterns = [
    
    path('',home, name='home'),
    # path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    
    
    
]