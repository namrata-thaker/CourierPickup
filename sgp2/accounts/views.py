from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .models import Account


# Create your views here.

def signup_view(request):
    if request.method =='POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            login(request,user)
            return redirect("/homepage/")
    form1 = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form1})

def login_view(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(data=request.POST)
        if form1.is_valid():
            user = form1.get_user()
            login(request,user)
            return  redirect("homepage/")

    else:
        form1 = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form1})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/accounts/")
def homepage(request):
   # return HttpResponse("homepag)
    email=request.POST["email"]
    password=request.POST["pass"]
    account=Account(email=email,password=password)
    account.save()
    return render(request,'accounts/homepage.html')
def index(request):
    return render(request,'accounts/index.html')
