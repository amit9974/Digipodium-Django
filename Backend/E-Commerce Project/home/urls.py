from django.urls import path, include
from . import views as home_views

urlpatterns = [
    
    path('', home_views.HomePage, name='home')
    
    
] 
