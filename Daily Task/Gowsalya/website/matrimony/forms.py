from . models import Bio,Sign
from django import forms

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields =[
            'username','password'
        ]

class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields =[
            'firstname','lastname','email','password'
        ]

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         widgets = {
#         'password': forms.PasswordInput(),
#     }