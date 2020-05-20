from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from datetime import datetime

class SignUpForm(forms.Form):
    username=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'}))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address *'}))
    city=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City Name *, Example: Banglore'}))
    company=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comapny Name *'}))
    category=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Category *'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'city', 'company', 'category')
