from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def Homepage(request):
    return render(request,'Pages/Index.html')