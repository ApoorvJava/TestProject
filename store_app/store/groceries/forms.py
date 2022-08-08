from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password')
        labels = {
            'username':'',
            'first_name':'',
            'last_name':'',
            'email':'',
            'password': '',
        }
        widgets= {
            'username': forms.TextInput(attrs={'placeholder':'Enter your username', 'style': 'width: 500px;', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder':'Enter your first name', 'style': 'width: 500px;', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Enter your last name', 'style': 'width: 500px;', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter your email address', 'style': 'width: 500px;', 'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your password(Atleast 8 characters)', 'autocomplete': 'off', 'style': 'width: 500px;', 'class': 'form-control'})
        }