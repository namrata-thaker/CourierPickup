from django.db import models

# Create your models here.
class Form(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    Address = models.TextField()
    City = models.CharField(max_length=10)
    Pincode = models.IntegerField()
    Mobile_No = models.IntegerField()
    Email = models.TextField()


class Sform(models.Model):
    RecieverName = models.CharField(max_length=10)
    Address = models.TextField()
    City = models.CharField(max_length=10)
    Pincode = models.IntegerField()
    Itype= models.CharField(max_length=15)
    Item_weight=models.IntegerField()



