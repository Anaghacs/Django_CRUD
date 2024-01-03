from django.shortcuts import render,redirect
from .models import Users

# Create your views here.
def index(request):
    mem=Users.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['email']
    d=request.POST['phone']
    e=request.POST['place']
    mem=Users(first_name=a,last_name=b,email_address=c,phone_no=d,place=e)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Users.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Users.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['email']
    d=request.POST['phone']
    e=request.POST['place']
    mem=Users.objects.get(id=id)
    mem.first_name=a
    mem.last_name=b
    mem.email_address=c
    mem.phone_no=d
    mem.place=e
    mem.save()
    return redirect("/")
