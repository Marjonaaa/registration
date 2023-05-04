from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

from .models import*

class AddProducts(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
User=get_user_model()       

class NewUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ("username",)       
        fields_classes = {'username':UsernameField}