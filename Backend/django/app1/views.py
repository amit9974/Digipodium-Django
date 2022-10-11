from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.


def homePage(request):
    movie = Movies.objects.all()[0:30]
    context={
        'movie':movie,
    }
    return render(request, 'index.html', context)

def ProductPage(request):
    return render(request, 'product.html')

def AboutPage(request):
    return render(request, 'about.html')

def SingerPage(request):
    return render(request, 'singer_info.html')

def pikachuPage(request):
    return render(request, 'ind.html')

def detailsPage(request, id):
    detail = Movies.objects.filter(id=id)
    context={
        'detail':detail,
    }
    return render(request, 'details.html', context)



"""Register User"""

def Register(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password1 = form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('homepage')

    else:
        form = CustomUser()
    context={
        'form':form,
    }

    return render(request, 'registration/register.html', context)