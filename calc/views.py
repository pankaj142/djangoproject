from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime

def home(request):
    return render(request,'home.html', {'name' :'Pankaj'})  
def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    result = num1 + num2
    return render(request, 'result.html',  { 'sum' : result})

def current_timedate(request):
    time = datetime.datetime.now()
    return HttpResponse(time)