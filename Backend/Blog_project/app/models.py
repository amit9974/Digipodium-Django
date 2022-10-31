from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='media/blog/images')
    caption = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.image.url



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sub_category(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name


class Article(models.Model):
    
    class StatusChoice(models.IntegerChoices):
        DRAFT = 0, 'DRAFT'
        PUBLISHED = 1, 'PUBLISHED'

    title = models.CharField(max_length=100, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,default=settings.AUTH_USER_MODEL)
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.DRAFT)
    tags = models.ManyToManyField(Tags)
    duration = models.DurationField()
    content = HTMLField()


    def __str__(self):
        return self.title