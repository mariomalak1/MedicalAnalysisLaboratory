from django.db import models

# Create your models here.

class MedicalAnalysis(models.Model):
    name = models.CharField(max_length=750)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Result(models.Model):
    medicalAnalysis = models.ForeignKey(MedicalAnalysis, on_delete=models.CASCADE)
    name = models.CharField(max_length=750)

    def __str__(self):
        return self.name

