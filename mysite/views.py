from django.shortcuts import render
import random

# Create your views here.
def mysite (request):
    return render(request,'home.html')

def bmi(request):
    return render(request,'bmi.html')

def lotto (request):
    number = str(random.randint(1,49))
    return render(request,'lotto.html',locals())

def news(request):
    return render(request,'news.html')

def course(request):
    return render(request,'course.html')

def teachers(request):
    return render(request,'teachers.html')

def admissions(request):
    return render(request,'admissions.html')
