from django.shortcuts import render

def Input(request):
    return render(request,'Views.html')

def Store(request):
    Fname=request.Post.get('Fname','')
    Lname=request.Post.get('Lname','')
    Email=request.Post.get('Email','')
    Address=request.Post.get('Add','')
    City=request.Post.get('City','')
    Country=request.Post.get('Country','')
    Zip=request.Post.get('Zip','')
    Phone=request.Post.get('Phone','')
    Text=request.Post.get('Text','')
    Data=request.Post.get('Data','off')