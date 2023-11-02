from django.forms import ModelForm
from .models import Contact, Registerfr
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Form(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class regauth(UserCreationForm):
  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(regauth, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        
        