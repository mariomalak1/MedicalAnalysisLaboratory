from django.db import models
from lab.models import Result, MedicalAnalysis
from app.models import Lab as appLab
# Create your models here.

class Patient(models.Model):
    Gender_choises = [
        ('Man', 'Man'),
        ('Women', 'Women'),
    ]

    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=5, choices=Gender_choises, default=Gender_choises[0].index("Man"))
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    dateTime = models.DateTimeField(auto_now=True, null=True, blank=True)
    medicalAnalysis = models.ManyToManyField(MedicalAnalysis)
    description = models.TextField(null=True, blank=True)
    patientDoctorName = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True, blank=True)
    done = models.BooleanField(default=False)
    address = models.CharField(max_length=250, null=True, blank=True)
    lab = models.ForeignKey(appLab, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def totalCost(self):
        all_cost = 0
        for i in self.medicalAnalysis.all():
            all_cost += i.price
        return all_cost


class Score(models.Model):
    result = models.ForeignKey(Result, on_delete= models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    score = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=11, null=True, blank=True)
    Address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


