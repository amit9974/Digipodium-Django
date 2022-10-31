from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tags)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Article)
admin.site.register(Image)



# @admin.register(Article)
# class Admin(admin.ModelAdmin):
#     '''Admin View for '''

#     list_display = ('title','author','category','status')
#     list_filter = ('author','category')
#     search_fields = ('title','author__username','category__name')
