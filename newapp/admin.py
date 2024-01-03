from django.contrib import admin
from .models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display="first_name","last_name","email_address","phone_no","place"

admin.site.register(Users,UsersAdmin)
