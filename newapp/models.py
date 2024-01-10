from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_address=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=12)
    place=models.CharField(max_length=50)

    
        