from django.shortcuts import render
from .models import *
from patient.models import Patient
from MedicalAnalysisLaboratory.settings import LAB_NAME, LOGO_PATH
# Create your views here.


def homePage(request):
    patient = Patient.objects.all().first()
    totalCost = patient.totalCost()
    context = {"title":"Mario Lab",
               "totalCost":totalCost,
               "LAB_NAME":LAB_NAME,
               "LOGO_PATH":LOGO_PATH,
               }
    return render(request, "base.html", context)




