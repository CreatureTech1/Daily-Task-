from django.db import models
class Contact(models.Model):
    name       = models.CharField(max_length=30)
    email      = models.EmailField() 
    mobileno   = models.IntegerField()
    address    = models.TextField(max_length=300)
    registerno = models.IntegerField()
    model      = models.CharField(max_length=30)
    color      = models.CharField(max_length=30) 