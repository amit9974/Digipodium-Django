from django.urls import path

from . import views as blog_view


urlpatterns = [
    path('', blog_view.HomePage, name='home'),
    path('new_post/', blog_view.NewPost, name='new_post'),
    path('details/<id>/', blog_view.Blog_details, name='details'),
    path('api/category/create/', blog_view.CategoryView, name='cat_create'),
]