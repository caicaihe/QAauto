from django.db import models

# Create your models here.


class envinfo(models.Model):
    Name = models.CharField( max_length=20, primary_key=True)
    IP = models.CharField( max_length=20)
    Registry = models.CharField(max_length=100)

class rfrecord(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField( max_length=20)
    envName = models.CharField( max_length=20)
    TestModel = models.CharField( max_length=20)
    email1 = models.CharField(max_length=100)
    email2 = models.CharField(max_length=100)
    email3 = models.CharField(max_length=100)
    TestTime = models.CharField( max_length=20)
    autopush = models.BooleanField(default=False)
