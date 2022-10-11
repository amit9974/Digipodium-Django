from tkinter.messagebox import RETRY
from turtle import RawTurtle
from django.shortcuts import redirect, render
from .models import *
import os
# Create your views here.

def HomePage(request):
    img = Images.objects.all()
    cat = Category.objects.all()
    context={
        'img':img,
        'cat':cat,
    }
    return render(request, 'index.html',context)


def add_category(request):
    pass

def add_image(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.POST['image']

        new_img = Images.objects.create(id=id, title=title, image=image)
        new_img.save()
        return redirect('/')
    else:
        return render(request, 'add_img.html')


def view_image(request,id):
    try:
        img = Images.objects.get(id=id)
        ctx ={
            'img':img
        }
        return render(request, 'image_view.html', ctx)
    except:
        return redirect('/')


def delete_image(request,id):
    # img = Images.objects.filter(id=id)
    # img.delete()
    # return redirect('/')
    try:
        img = Images.objects.get(id=id).delete()
        os.remove(img.images.path)
        img.delete()
        return redirect('/')
    except:
        print('Error deleting image')
    return redirect('/')