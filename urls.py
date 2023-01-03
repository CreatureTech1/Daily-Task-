from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.get_user_profile),
]