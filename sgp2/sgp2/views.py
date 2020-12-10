from django.http import HttpResponse
from django.shortcuts import render
#from .models import Account


def about(request):
    #return HttpResponse("about")
    return render(request,'about.html')


