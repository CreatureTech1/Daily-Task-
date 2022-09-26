from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'aadiran.html')

def payment(request):
    return render(request,'payment.html')

