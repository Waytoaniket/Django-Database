from django.shortcuts import render
from django.http import HttpResponse
from .models import Database

def Input(request):
    return render(request,'Views.html')

def Store(request):
    Fname=request.POST.get('Fname','')
    print(Fname)
    Lname=request.POST.get('Lname','')
    print(Lname)
    Email=request.POST.get('Email','')
    print(Email)
    Address=request.POST.get('Add','')
    print(Address)
    City=request.POST.get('City','')
    print(City)
    Country=request.POST.get('Country','')
    print(Country)
    Zip=request.POST.get('Zip','')
    print(Zip)
    Phone=request.POST.get('Phone','')
    print(Phone)
    Text=request.POST.get('Text','')
    print(Text)
    seedata=request.POST.get('Seedata','off')
    print(seedata)

    Store= Database (Fname=Fname,Lname=Lname,Email=Email,Add=Address,city=City,Country=Country,Zip=Zip,Phone=Phone,Text=Text)
    Store.save()
    return HttpResponse('hello')