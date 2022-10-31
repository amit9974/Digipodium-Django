from django import forms
from .models import *

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, help_text='Enter a category name')


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),empty_label='Select Category'
    )
    
    