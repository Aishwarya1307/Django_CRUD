from django.shortcuts import render
from django.db import connection
from .models import CUSTOMER_INFO

def home(request):
    return render(request, "Home/Home.html")


def customer(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from django_app_customer_info")
        context =  cursor.fetchall()
        print(context)
    return render(request, "Home/all_customers.html" , context={"customers": context})


def add_new(request):
    if request.method == "POST":
        customer_name = request.POST['customer_name']
        Email = request.POST['Email']
        Phone_number = request.POST['Phone number']
        password = request.POST['Password']
        city = request.POST['city']

        new_customer = CUSTOMER_INFO(customer_name = customer_name ,Email_id= Email,Phone_number = Phone_number,Password= password, City=city)
        new_customer.save()
    return render(request,"Home/add_new.html",{})
