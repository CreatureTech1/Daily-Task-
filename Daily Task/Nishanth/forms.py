from . models import Contact 
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = [
            'name','email','mobileno','address','registerno','model','color'
        ]