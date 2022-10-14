from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


#Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method =='POST':
        Uform=UserCreationForm(request.POST)
        if Uform.is_valid():
            Uform.save()
        return redirect('login')
    else:
            Uform=UserCreationForm
    return render(request,'registration/register.html',{'form':Uform}) 
def LoginView(request) :
    return render(request,'login.html') 
#def LogoutView(request):
    #return render(request,'index.html')
      
        
@login_required     
def profile(request):
     return render(request,'profile.html') 
     
    
    

