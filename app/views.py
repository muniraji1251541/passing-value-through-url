from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def logan(request,name):
    return HttpResponse(f'Welcome to here {name}')