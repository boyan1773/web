from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'home.html')

def news(request):
    return render(request,'news.html')

def course(request):
    return render(request,'course.html')

def teachers(request):
    return render(request,'teachers.html')

def admissions(request):
    return render(request,'admissions.html')
