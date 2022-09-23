from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('app/signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home.html', views.home, name='home'),
    path('bussearch.html', views.bussearch, name='bussearch'),
    path('booking.html', views.booking, name='booking'),
    path('bookinglist.html', views.bookinglist, name='bookinglist'),
]






