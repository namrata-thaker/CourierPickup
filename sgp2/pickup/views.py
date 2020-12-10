from django.shortcuts import render
from.models import Form,Sform

# Create your views here.
def order(request):
    all_order=Sform.objects.all()
    return render(request,'pickup/order.html', {'orders':all_order})

def shipment(request):
    FirstName=request.POST.get('FirstName')
    LastName=request.POST.get('LastName')
    Address =request.POST.get('Address')
    City=request.POST.get('City')
    Pincode=request.POST.get('Pincode')
    Mobile_No=request.POST.get('Mobile_No')
    Email=request.POST.get('Email')
    form1=Form(FirstName=FirstName,LastName=LastName,Address=Address,City=City,Pincode=Pincode,Mobile_No=Mobile_No,Email=Email)
    form1.save()
    return render(request,'pickup/shipment.html')

def form(request):
    return render(request,'pickup/form.html')

def success(request):
    RecieverName=request.POST['RecieverName']
    Address =request.POST['Address']
    City=request.POST['City']
    Pincode=request.POST['Pincode']
    Itype=request.POST['Itype']
    Item_weight=request.POST['Item_weight']
    form2=Sform(RecieverName=RecieverName,Address=Address,City=City,Pincode=Pincode,Itype=Itype,Item_weight=Item_weight)
    form2.save()
    return render(request,'pickup/success.html')

def header(request):
    return render(request,'pickup/header.html')
