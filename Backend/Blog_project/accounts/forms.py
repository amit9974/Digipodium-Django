from django import forms
from django.contrib.auth.models import User


INVALID_USERNAMES = ['admin','administrator','root']

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# register form
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Choose Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email


# from django import forms
# from django.contrib.auth.models import User

# #Login Form
# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(
#         widget=forms.PasswordInput()
#     )
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email__iexact=email)  #handle Uper & lower case like Amit or amit
#         if not qs.exists():
#             raise forms.ValidationError('Invalid Credntials')
#         return email


# INVALID_USERNAMES = ['administrator','root']

# #Register Form
# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.PasswordInput()
#     password2 = forms.PasswordInput()

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username__iexact=username)
#         if qs.exists():
#             raise forms.ValidationError('Username is already exists')
#         if username.lower() in INVALID_USERNAMES:
#             raise forms.ValidationError('Username not allowed')
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email__iexact=email)
#         if qs.exists():
#             raise forms.ValidationError('Email already exists')
#         return email

        