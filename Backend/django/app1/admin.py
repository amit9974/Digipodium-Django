from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Weather)

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    '''Admin View for Movies'''

    list_display = ('name','actor','release_date')
    list_filter = ('release_date','name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name','klass','roll_number')
    list_filter = ('klass','name')
    search_fields = ('name',)
 

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('student','english','hindi','science','computer','math')
    

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    '''Admin View for Singer'''

    list_display = ('first_name','last_name','language')
    list_filter = ('first_name','language')
    search_fields = ('first_name','language')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    '''Admin View for Song'''

    list_display = ('title','singer')
    list_filter = ('singer',)