from django.shortcuts import render,redirect
from .models import Users
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    user=Users.objects.all()
    return render(request,'index.html',{'user':user})

def add(request):
    return render(request,'add.html')


def addrec(request):
    first_name=request.POST['first']
    last_name=request.POST['last']
    email_id=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    user=Users(first_name=first_name,last_name=last_name,email_address=email_id,phone_no=phone,place=place)
    user.save()
    return redirect("/")

def delete(request,id):
    user=Users.objects.get(id=id)
    user.delete()
    return redirect("/")

def update(request,id):
    user=Users.objects.get(id=id)
    return render(request,'update.html',{'user':user})

def uprec(request,id):
    first_name=request.POST['first']
    last_name=request.POST['last']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    user=Users.objects.get(id=id)
    user.first_name=first_name
    user.last_name=last_name
    user.email_address=email
    user.phone_no=phone
    user.place=place
    user.save()
    return redirect("/")