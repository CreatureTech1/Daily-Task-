from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model =User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email'
        }
    def save(self,commit=True):
        User =super(RegisterForm,self).save(commit=False)
        User.first_name=self.cleaned_data['first_name']
        User.last_name=self.cleaned_data['last_name']
        User.email_name=self.cleaned_data['email']
        if commit:
            User.save()
        return User    
        