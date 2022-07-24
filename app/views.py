import datetime

from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def index(request):
    if request.method == "POST":
        if request.POST.get("regNumber"):
            regNumber = request.POST.get("regNumber")
            patient = Patient.objects.get(regNumber = regNumber)
            return redirect('complaint', slug = patient.regNumber)
    context = {}
    return render(request, 'index.html', context)


def registration(request):
    registerForm = RegisterForm

    if request.method == "POST":
        registerForm = registerForm(request.POST)
        if registerForm.is_valid():

            obj=registerForm.save(commit=False)
            obj.regNumber=f'{obj.firstName}210'
            print('dddd', obj.regNumber)
            obj.save()
            registerForm = RegisterForm
            return redirect('complaint', slug = obj.regNumber)

    context = {"RegisterForm": registerForm}
    return render(request, 'Registration.html', context)


def complaints(request, slug):
    patient = Patient.objects.get(regNumber = slug)
    if request.method == "POST":
        if request.POST.get("complain"):
            # regNumber = request.POST.get("complain")
            feeling = request.POST.get('feeling')
            painLevel = request.POST.get('painLevel')
            doc = request.POST.get('doc')
            sex = request.POST.get('sex')
            Complaint.objects.create(
                patient = patient,
                feeling = feeling,
                painLevel = 10,
                selectDoctor = doc
            )
            return redirect('doctor', slug = patient.id)





    context = {'patient': patient, }
    return render(request, 'complaint.html', context)


def doctor(request, slug):
    patient = Patient.objects.get(id = slug)
    complain = Complaint.objects.get(patient = patient)
    context = {'patient': patient, 'complain': complain}
    return render(request, 'DocPage.html', context)