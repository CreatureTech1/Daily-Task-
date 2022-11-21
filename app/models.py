from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponse

class EnqInsert(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    travel_destination = models.CharField(max_length=150)
    date = models.DateTimeField(editable=True, auto_now_add=True)
    no_of_person = models.IntegerField()
    vacation_type = models.CharField(max_length=150)
    class Meta:
        db_table = 'enquireform'    

class Subscription(models.Model):
    mail = models.CharField(max_length=150)
    class Meta:
        db_table = 'subscribe'

