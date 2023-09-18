from django.db import models

# Create your models here.



class Users(models.Model):
    name = models.CharField(max_length=32)
    Department = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    ways= models.CharField(max_length=64)



