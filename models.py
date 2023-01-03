from django.db import models

# Create your models here.
class UserDetails(models.Model):
    userid = models.IntegerField
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


from django.db import models

class FacebookResponse(models.Model):
    facebook_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    