from django.shortcuts import render
from .models import Users

# Create your views here.
def index(request):
    mem=Users.objects.all()
    return render(request,'index.html',{'mem':mem})
