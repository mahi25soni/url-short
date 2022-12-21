from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User 
from .models import *
 
class MyUser(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passoword'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
    )

class URLForm(forms.ModelForm):
    class Meta:
        model = ALLurl
        fields = ['url']
        widgets = {
            'url': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your URL'}),
        }