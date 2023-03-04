from django.shortcuts import render
from .models import *
from patient.models import Patient
# Create your views here.

def homePage(request):
    patient = Patient.objects.all().first()
    totalCost = patient.totalCost()
    context = {"title":"Mario Lab",
               "totalCost":totalCost}
    return render(request, "base.html", context)




