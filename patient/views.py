from django.shortcuts import render
from .models import *
# Create your views here.

def addPatient(request):
    pass

def allPatients(request):
    patients = Patient.objects.all()
    context = {"patients":patients}
    return render(request, "patient/allPatient.html", context)