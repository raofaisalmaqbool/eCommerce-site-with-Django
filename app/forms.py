from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerRegistrationFrom(UserCreationForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form_control'}))
    password2= forms.CharField(label='Canfirm Password', widget=forms.PasswordInput(attrs={'class':'form_control'}))
    email= forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form_control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

