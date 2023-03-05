from django.shortcuts import render
from .models import *
from MedicalAnalysisLaboratory.settings import LAB_NAME, LOGO_PATH
# Create your views here.

def addPatient(request):
    pass

def allPatients(request):
    patients = Patient.objects.all()
    context = {"patients":patients,
               "LAB_NAME":LAB_NAME,
               "LOGO_PATH":LOGO_PATH,
               }
    return render(request, "patient/allPatient.html", context)