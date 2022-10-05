from pyexpat import model
from django.shortcuts import render ,redirect
from .form import loginform
from .models import Login
from django.contrib import auth

def login(request):
    form = loginform(request.POST or None)
    if form.is_valid():
        account = request.POST.get('account_name', '')
        password = request.POST.get('password_name', '')
        modelspassword = Login.objects.filter(account_name=account)
        print(modelspassword)
        if password == modelspassword:
            return redirect('/home')

    context = {
        'form':form
    }

    return render(request,'login.html',context)
