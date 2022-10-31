from django import forms
from .models import Category, Tags, Image, Article
from tinymce.widgets import TinyMCE

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ('name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'row':20}))
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple)
    # status = forms.ModelMultipleChoiceField(queryset=STA.objects.all(), widget=forms.CheckboxSelectMultiple)
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
        
    class Meta:
        model = Article
        fields = ('title','content','category','tags','status','duration')

# class BlogForm(forms.Form):
#     author = forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Select Author')
#     caption = forms.CharField(max_length=100)
#     post = forms.CharField(max_length=200)
#     image = forms.ImageField()
#     tag = forms.ModelChoiceField(queryset=Tags.objects.all(),empty_label='Select Tag')
   

        