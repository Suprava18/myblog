from django.shortcuts import render

def home(request):
    return render(request,"about.html")

def academics(request):
    return render(request,"academics.html")

def new(request):
    return render(request,"new.html")

def test(request):
    return render(request,'test.html')

    
