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
    form = ComplainForm
    if request.method == "POST":
        form = ComplainForm(request.POST)
        if form.is_valid():

            obj=form.save(commit=False)
            obj.patient = patient
            obj.save()
            return redirect('doctor', slug = obj.id)
        else:
            print(form.errors)

    context = {'patient': patient, "form": form}
    return render(request, 'complaint.html', context)


def doctor(request, slug):
    complain = Complaint.objects.get(id=slug)

    form = DocForm
    if request.method == 'POST':
        form = DocForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.complain = complain
            obj.save()
            return redirect('lab', slug = complain.id)

    patient_id = complain.patient.id
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'complain': complain, "form": form}
    return render(request, 'DocPage.html', context)


def lab(request, slug):
    complain = Complaint.objects.get(id=slug)

    form = LabForm
    if request.method == 'POST':
        form = LabForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.complain = complain
            obj.save()
            # return redirect('doctor', slug = obj.id)
    doctorNote = Doctor.objects.get(complain = complain)
    patient_id = complain.patient.id
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'complain': complain, "form": form, 'doctor': doctorNote}
    return render(request, 'lab.html', context)