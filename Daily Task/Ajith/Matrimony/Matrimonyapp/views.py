from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"matrimony.html")

def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")

def vehicle(request):
    return render(request,"vehicle.html")

def driver(request):
    return render(request,"driver.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def driverlogin(request):
    return render(request,"driverlogin.html")