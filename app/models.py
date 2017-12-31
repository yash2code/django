from django.db import models

# Create your models here.

class Profile(models.Model):
   name = models.CharField(max_length=20, blank=False, null=False)



   


