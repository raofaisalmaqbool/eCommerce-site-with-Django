from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class CustomerRegistrationFrom(UserCreationForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form_control'}))
    password2= forms.CharField(label='Canfirm Password', widget=forms.PasswordInput(attrs={'class':'form_control'}))
    email= forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form_control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'} 
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password: forms.Field = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomlete':'current-password', 'class':'form-control'}))
