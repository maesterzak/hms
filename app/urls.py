from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('complaint/<slug:slug>/', complaints, name = 'complaint'),
    path('register/', registration, name = 'register'),
    path('complain//<slug:slug>/doctor/', doctor, name = 'doctor'),
    path('complain/<slug:slug>/doctor/lab/', lab, name = 'lab'),
    path('complain/<slug:slug>/doctor/pharmacy/', pharmacy, name = 'pharmacy'),
    path('complain/<slug:slug>/billing/', billing, name = 'billing'),


]