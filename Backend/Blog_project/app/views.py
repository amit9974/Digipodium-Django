from unicodedata import category
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.conf import settings
from .forms import ArticleForm, CategoryForm, ImageForm, TagsForm
# Create your views here.

def HomePage(request):
    article = Article.objects.all()
    cat = Category.objects.all()
    sub = Sub_category.objects.all()
    ctx={
        'article':article,
        'cat':cat,
        'sub':sub,
   }
    return render(request, 'blog/index.html', ctx)


def NewPost(request):
    article_form = ArticleForm(request.POST or None)
    cat_form = CategoryForm()
    image_form = ImageForm()
    tag_form  = TagsForm()
    if article_form.is_valid():
        
        article_form = article_form.save(commit=False)
        article_form.author = request.user
        article_form.save()
        messages.success(request, 'New post added')
        return redirect('/')

    ctx = {
        'article_form':article_form,
        'cat_form':cat_form,
        'image_form':image_form,
        'tag_form':tag_form,
    }
    return render(request, 'blog/create_post.html', ctx)


def CategoryView(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            cat = category_form.save(commit=False)
            cat.save()
            return JsonResponse({'status':'success', 'name':cat.name, 'id':cat.id})
        else:
            return JsonResponse({'status':'error'})
    else:
        return JsonResponse({'status':'Invalid data'})

    # cat_form = CategoryForm(request.POST or None)
    # article_form = ArticleForm()
    # image_form = ImageForm()
    # tag_form  = TagsForm()
    # if cat_form.is_valid():
    #     cat_form.save()
    #     messages.success(request, 'New Category has been added')
    #     return redirect('/')
    # ctx={
    #     'cat_form':cat_form,
    #     'article_form':article_form,
    #     'image_form':image_form,
    #     'tag_form':tag_form,
    # }
    # return render(request, 'blog/index.html',ctx)

def TagsView(request):
    pass


def ImageUploadView(request):
    pass


# def NewPost(request):
#     form = BlogForm()
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             author = form.cleaned_data['author']
#             caption = form.cleaned_data['caption']
#             post = form.cleaned_data['post']
#             image = form.cleaned_data['image']
#             tag = form.cleaned_data['tag']
           
#             blog = Article(author=author,caption=caption,post=post,image=image,tag=tag)
#             blog.save()
#             messages.success(request, 'New Post Added')
#             return redirect('/')
#     else: 
#         messages.error(request, 'Error 404')
#     ctx={
#         'form':form
#     }
#     return render(request, 'blog/create_post.html', ctx)


def Blog_details(request, id):
    blog = Article.objects.filter(id=id)
    ctx={'blog':blog}
    return render(request, 'blog/details_page.html',ctx)