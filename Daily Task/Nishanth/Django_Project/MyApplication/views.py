from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    
    return render(request,'home.html')

def register(request):
    if request.method == 'Post' :
        form =UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            form=UserCreationForm() 
           
        return render(request,'registration.html',{'form':form})          