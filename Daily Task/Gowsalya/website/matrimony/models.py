from django.db import models

class Bio(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Sign(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)


