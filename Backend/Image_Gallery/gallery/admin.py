from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    '''Admin View for Images'''

    list_display = ('title','category')
    list_filter = ('category',)
    search_fields = ('category','title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
