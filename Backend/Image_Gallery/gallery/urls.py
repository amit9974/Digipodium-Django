from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('add_img/',views.add_image, name='add_img'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete/<int:id>/', views.delete_image, name='delete'),
    path('view_image/<int:id>/', views.view_image, name='view_image')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
