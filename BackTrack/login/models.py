from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100, blank=True)
    password=models.CharField(max_length=100, blank=True)
    userType=models.IntegerField(blank=True)

class currentUser(models.Model):
    username=models.CharField(max_length=100, blank=True)
    password=models.CharField(max_length=100, blank=True)
    userType=models.IntegerField(blank=True)