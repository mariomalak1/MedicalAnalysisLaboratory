from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lab(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    phoneNumber = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.name

class LabUser(models.Model):
    name = models.CharField(max_length= 150)
    lab = models.ForeignKey(Lab, on_delete= models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=11, null = True, blank=True)
    salary = models.PositiveIntegerField(null = True, blank=True)
    adminCreateBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name