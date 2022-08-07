from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Complaint)
admin.site.register(Doctor)
admin.site.register(Pharmacy)
admin.site.register(Lab)
admin.site.register(LabItems)