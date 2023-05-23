from django.db import models

# Create your models here.

class Customer(models.Model):
    cno = models.IntegerField()
    cname = models.CharField(max_length=100)
    cmobile = models.IntegerField()
    cemail = models.EmailField()
    cbankname = models.CharField(max_length=30)
    caccountnumber = models.IntegerField()
    caccountifsccode = models.CharField(max_length=9)

