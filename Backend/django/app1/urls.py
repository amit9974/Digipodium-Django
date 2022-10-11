from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.homePage, name='homepage'),
    path('product/', views.ProductPage, name='product'),
    path('about/', views.AboutPage, name='about'),
    path('singer/', views.SingerPage, name='singer'),
    path('ind/', views.pikachuPage, name='ind'),
    path('details/<int:id>/', views.detailsPage, name='details'),
    path('register/', views.Register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)