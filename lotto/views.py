from django.shortcuts import render
import random


# Create your views here.
def lotto (request):
    number = str(random.randint(1,49))
    return render(request,'lotto.html',locals())

