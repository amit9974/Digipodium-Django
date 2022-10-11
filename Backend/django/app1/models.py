from django.db import models
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(auto_created=True, null=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    actor = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to='Movies_image/', null=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    klass = models.IntegerField(verbose_name='class')
    roll_number = models.IntegerField()

    def __str__(self):
        return self.name


class Report(models.Model):
    english = models.IntegerField()
    hindi = models.IntegerField()
    science = models.IntegerField()
    math = models.IntegerField()
    computer = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'Report of {self.student.name}'

class Weather(models.Model):
    temp = models.DecimalField(decimal_places=2, max_digits=10)
    wind_speed = models.DecimalField(decimal_places=2, max_digits=10)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Temp of Today {self.temp}"



class Singer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + " "+ self.last_name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




"""New User Class"""
class CustomUser(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address', error_messages={'exists':'Email is already exists'})
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


    def __init__(self, *args, **kwargs) -> None:
        super(CustomUser, self).__init__(*args, **kwargs)

        """Placeholder"""
        self.fields['username'].widget.attrs['placeholder'] = 'Username *'
        self.fields['email'].widget.attrs['placeholder'] = 'Email *'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


    def save(self, commit=True):
        user = super(CustomUser, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('Email is already exists')
        return self.cleaned_data['email']

        