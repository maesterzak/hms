from django import forms
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(ModelForm):
    class Meta:
        model=Patient
        fields = '__all__'
        exclude = ['regNumber']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['firstName'].widget.attrs['placeholder'] = 'Enter your First Name'
        self.fields['middleName'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['middleName'].widget.attrs['placeholder'] = 'Enter your Middle Name'
        self.fields['lastName'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['lastName'].widget.attrs['placeholder'] = 'Enter your Last Name'
        self.fields['dateOfBirth'] = forms.DateField(widget=DateInput)

        self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Enter your phone number'

        self.fields['email'].widget.attrs['class'] = 'form-control form-control-email'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email'


class ComplainForm(ModelForm):
    class Meta:
        model=Complaint
        fields = '__all__'
        exclude = ['patient']

    def __init__(self, *args, **kwargs):
        super(ComplainForm, self).__init__(*args, **kwargs)


class DocForm(ModelForm):
    class Meta:
        model=Doctor
        fields = '__all__'
        exclude = ['complain']

    def __init__(self, *args, **kwargs):
        super(DocForm, self).__init__(*args, **kwargs)


class LabItemsForm(ModelForm):
    class Meta:
        model=LabItems
        fields = '__all__'
        exclude = ['lab']

    def __init__(self, *args, **kwargs):
        super(LabItemsForm, self).__init__(*args, **kwargs)


class PharmacyItemsForm(ModelForm):
    class Meta:
        model=PharmacyItems
        fields = '__all__'
        exclude = ['pharmacy']

    def __init__(self, *args, **kwargs):
        super(PharmacyItemsForm, self).__init__(*args, **kwargs)        

