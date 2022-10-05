from tkinter.filedialog import SaveAs
from django.shortcuts import render , redirect
from .form import registerform
from login.models import Login
def register(request):
    form = registerform(request.POST or None)
    if form.is_valid():
        account = request.POST.get('account_name', '')

        form.save()
        form = registerform()
        return redirect ('/login/')
    context = {
        'form':form
    }
    return render(request,'register.html',context)

