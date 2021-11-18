from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Contact(models.Model):
    contactID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

class Error(models.Model):
    errorID = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000)
    explination = models.CharField(max_length=1000)
    fix = models.CharField(max_length=1000)

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    class meta:
        db_table = 'tbluser'            

class Agent(AbstractUser):
    agentID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    class meta:
        db_table = 'tblagent'            