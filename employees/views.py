from django.shortcuts import HttpResponse
from .models import Employees

def index(request):
    return HttpResponse("Hello bro!")