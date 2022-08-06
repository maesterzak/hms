from django.db import models

# Create your models here.

class Patient(models.Model):
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    GENOTYPE_CHOICES = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS'),
        ('AC', 'AC')
    )


    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    genoType = models.CharField(
        'Genotype',
        max_length=10,
        choices=GENOTYPE_CHOICES,
        default='AA')
    bloodGroup = models.CharField(
        'Genotype',
        max_length=10,
        choices=BLOOD_GROUP_CHOICES,
        default='A+')
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField()
    gender = models.CharField(
        'Gender',
        max_length=10,
        choices=GENDER_CHOICES,
        default='M'
    )
    regNumber = models.CharField(max_length=200, default='1234566.7')
    nextOfKinFullName = models.CharField(max_length=300)
    nextOfKinPhoneNumber = models.CharField(max_length=11)
    nextOfKinEmail = models.EmailField()


class Complaint(models.Model):
    # DOCTOR_CHOICES =(
    #     ('General Consultant ', 'General Consultant'),
    #     ('General Consultant ', 'General Consultant'),
    #     ('General Consultant ', 'General Consultant'),
    #     ('General Consultant ', 'General Consultant'),
    #
    # )
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    # selectDoctor = models.CharField(
    #     'Doctor',
    #     max_length=30,
    #     choices=DOCTOR_CHOICES,
    #     default= 'General Consultant'
    # )
    nurse = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    temperature = models.IntegerField()
    bloodPressure = models.IntegerField()



class Doctor(models.Model):
    complain = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    doctorNote = models.TextField(null=True,blank=True)
    patientComplain = models.TextField()
    suggested_lab_test = models.TextField(null=True, blank=True)
    suggested_drug_test = models.TextField(null=True, blank=True)


class Lab(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    test_run = models.CharField(max_length=200)
    amount = models.IntegerField()


class Pharmacy(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    drug = models.CharField(max_length=200)
    amount = models.IntegerField()


class Bill(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    doctor_consultancy_fee = models.IntegerField()
    laboratory_fee = models.IntegerField()
    pharmacy_fee = models.IntegerField()

