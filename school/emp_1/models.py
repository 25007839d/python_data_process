from django.db import models

# Create your models here.

class emp(models.Model):
    name = models.CharField(max_length=99)
    eid = models.IntegerField
    city = models.CharField(max_length=50)
    dept = models.CharField(max_length=30)
