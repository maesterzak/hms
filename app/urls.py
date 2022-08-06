from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('complaint/<slug:slug>/', complaints, name = 'complaint'),
    path('register/', registration, name = 'register'),
    path('complain/doctor/<slug:slug>/', doctor, name = 'doctor'),
    path('complain/doctor/lab/<slug:slug>/', lab, name = 'lab'),

]