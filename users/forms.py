from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class SingUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),label = "Userriz ni kiriting")
    password1  = forms.CharField(widget=forms.PasswordInput(attrs={'class':"input"}),label="Kodni kirirting")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"input"}),label="Takroran kodni kiriting")

    class Meta:
        model =User
        fields = ['username','password1','password2']


class SingInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}), label="Userriz ni kiriting")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "input"}), label="Kodni kirirting")


    class Meta:
        model =User
        fields = ['username','password']