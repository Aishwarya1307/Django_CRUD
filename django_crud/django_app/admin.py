from django.contrib import admin
from .models import CUSTOMER_INFO
# Register your models here.

@admin.register(CUSTOMER_INFO)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ('id','customer_name', 'email_id','phone_number',"password",'city','created_time')