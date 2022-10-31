
from django.urls import path, include
from .views import Do_Login, RegisterUserForm

urlpatterns = [

    path('login/', Do_Login, name='login'),
    path('register/', RegisterUserForm, name='register'),
    # path('accounts/',include('django.contrib.auth.urls')),

]


# from django.urls import path, include
# from .views import Do_Login, RegisterUserForm

# urlpatterns = [
#     path('login/', Do_Login, name='login'),
#     path('register/', RegisterUserForm, name='register'),

# ]