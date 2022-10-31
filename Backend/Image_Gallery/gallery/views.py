from unicodedata import category
from django.shortcuts import redirect, render
from .models import *
import os
from .forms import ImageUploadForm, CategoryForm
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
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Category.objects.create(name=name)
            cat.save()
            return redirect('/')

    ctx ={
        'form':form
    }
    return render(request, 'add_cat.html', ctx)


def add_image(request):
    form = ImageUploadForm()
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            image = Images(title=title, category=category, image=image)
            image.save()
            return redirect('/')
    ctx={
        'form':form,
    }
    return render(request, 'add_img.html',ctx)


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