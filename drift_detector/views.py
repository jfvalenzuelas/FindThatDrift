from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.utils import timezone

def home(request):
    return render(request, 'drift_detector/home.html')