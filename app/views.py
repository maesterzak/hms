import datetime
from multiprocessing import context
from django.http import HttpResponse

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
    
    doctorSample = Doctor.objects.filter(complain = complain.id).first()
    if doctorSample is None:

        form = DocForm
        
    else:
        
        form = DocForm(instance = doctorSample)
    
    
    if request.method == 'POST':
        if doctorSample is None:
            form = DocForm(request.POST)
            
        else:
            
            form = DocForm(request.POST, instance = doctorSample)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.complain = complain
            obj.save()
            if request.POST.get("lab"):
                return redirect('lab', slug = complain.id)
            elif request.POST.get("pharmacy"):
                   return redirect('pharmacy', slug = complain.id) 
            else:
                return HttpResponse('ERROR PAGE DOES NOT EXIST')       

    patient_id = complain.patient.id
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'complain': complain, 'form': form}
    return render(request, 'DocPage.html', context)


def lab(request, slug):
    complain = Complaint.objects.get(id=slug)
    labInstance, created = Lab.objects.get_or_create(complaint = complain)
    lab_tests = LabItems.objects.filter(lab = labInstance)

    total = 0
    
    
    form = LabItemsForm
    if request.method == 'POST':
        
        form = LabItemsForm(request.POST)
        if form.is_valid():
            
            obj=form.save(commit=False)
            obj.lab = labInstance
            obj.save()
            form = ''
            # return redirect('doctor', slug = obj.id)
    form = LabItemsForm        
    doctorNote = Doctor.objects.get(complain = complain)
    for test in lab_tests:
        total += test.amount
    total = total
    patient_id = complain.patient.id
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'complain': complain, "form": form, 'doctor': doctorNote, 'labTests': lab_tests, 'total': total}
    return render(request, 'lab.html', context)


def pharmacy(request, slug):
    complain = Complaint.objects.get(id=slug)
    pharmacyInstance, created = Pharmacy.objects.get_or_create(complaint = complain)
    pharmacy_items = PharmacyItems.objects.filter(pharmacy = pharmacyInstance)

    total = 0
    
    
    form = PharmacyItemsForm
    if request.method == 'POST':
        
        form = PharmacyItemsForm(request.POST)
        if form.is_valid():
            
            obj=form.save(commit=False)
            obj.pharmacy = pharmacyInstance
            obj.save()
            form = ''
            # return redirect('doctor', slug = obj.id)
    form = PharmacyItemsForm        
    doctorNote = Doctor.objects.get(complain = complain)
    for items in pharmacy_items:
        total += items.amount
    
    patient_id = complain.patient.id
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient, 'complain': complain, "form": form, 'doctor': doctorNote, 'pharmacyItems': pharmacy_items, 'total': total}
    return render(request, 'pharmacy.html', context)



def billing(request, slug):
    consultancyFee = 300
    labTotal = 0
    pharmacyTotal = 0
    complain = Complaint.objects.get(id=slug)
    lab = Lab.objects.filter(complaint = complain.id).first()
    if lab is not None:
        lab_tests = LabItems.objects.filter(lab = lab)
        for test in lab_tests:
            labTotal += test.amount
    pharmacy = Pharmacy.objects.filter(complaint = complain.id).first()
    
    if pharmacy is not None:
        pharmacyItems = PharmacyItems.objects.filter(pharmacy = pharmacy)
        for item in pharmacyItems:
            pharmacyTotal += item.amount
    
    total = pharmacyTotal + labTotal + consultancyFee    
     
    context = {'labTotal': labTotal, 'total': total, 'pharmacyTotal': pharmacyTotal, 'consultancyFee': consultancyFee}
    
    return render(request, 'billing.html', context)
