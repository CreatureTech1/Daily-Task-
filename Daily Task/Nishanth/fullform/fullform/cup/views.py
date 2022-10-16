from contextlib import redirect_stderr

#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from cup.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
            form =RegisterForm()

    return render(request,'registration/register.html',{'form':form})
