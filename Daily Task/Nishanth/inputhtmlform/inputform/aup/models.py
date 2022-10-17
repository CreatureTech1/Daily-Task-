from django.db import models


# Create your models here.
class inputform(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    
    def _str_(self):
        return self.title
