from django.db import models

class Reg(models.Model):
    name = models.CharField(max_length=30)
    mailid = models.EmailField(max_length=30)
    mobile = models.IntegerField()
    address = models.TextField(max_length=50)
    registration_number= models.IntegerField()
    model = models.CharField(max_length=30)
    make_of_vehicle = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField()
    current_mileage = models.CharField(max_length=30)
    dealer_name = models.CharField(max_length=30)


class Driver(models.Model):
    name=models.CharField(max_length=30)
    mailid=models.EmailField(max_length=30)
    phone=models.IntegerField()

