from django.db import models

# Create your models here.

class Account(models.Model):
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=10)

     def __str__(self):
         return self.email
         return self.password