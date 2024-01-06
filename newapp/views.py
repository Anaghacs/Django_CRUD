from django.shortcuts import render,redirect
from .models import Users

# Create your views here.
def index(request):
    user=Users.objects.all()
    return render(request,'index.html',{'user':user})

def add(request):
    return render(request,'add.html')

def addrec(request):
    if request.method=="POST":
        first_name=request.POST['first']
        last_name=request.POST['last']
        email=request.POST['email']
        phone=request.POST['phone']
        place=request.POST['place']
        user=Users(first_name=first_name,last_name=last_name,email_address=email,phone_no=phone,place=place)
        user.save()
    return redirect("/")

def delete(request,id):
    mem=Users.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    user=Users.objects.get(id=id)
    return render(request,'update.html',{'user':user})

def uprec(request,id):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['email']
    d=request.POST['phone']
    e=request.POST['place']
    user=Users.objects.get(id=id)
    user.first_name=a
    user.last_name=b
    user.email_address=c
    user.phone_no=d
    user.place=e
    user.save()
    return redirect("/")
