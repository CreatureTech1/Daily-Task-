from django.forms import ModelForm
from . models import Reg,Driver
from django import forms



class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields =[
            'name','mailid','mobile','address','registration_number','model','make_of_vehicle','color','year','current_mileage','dealer_name'
        ]


class DriverForm(forms.ModelForm):
    class Meta:
        model= Driver
        fields= ['name','mailid','phone']