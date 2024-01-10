from http.client import HTTPException
from django.shortcuts import render,redirect
from django.db import connection
from .models import CUSTOMER_INFO
from datetime import datetime
from loguru import logger
from django.shortcuts import redirect

def home(request):
    return render(request, "Home/Home.html")


def customer(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("select * from django_app_customer_info")
            context =  cursor.fetchall()
            print(context)
        return render(request, "Home/all_customers.html" , context={"customers": context})
    
    except HTTPException as e:
        logger.debug(f'{e}')
        raise e



def add_new(request):
    try:
        if request.method == "POST":
            customer_name = request.POST['customer_name']
            email = request.POST['email']
            phone_number = request.POST['phone number']
            password = request.POST['password']
            city = request.POST['city']

            new_customer = CUSTOMER_INFO(customer_name = customer_name ,email_id= email,phone_number = phone_number,password= password, city=city, created_time= str(datetime.now()))
            new_customer.save()
            return redirect("all_customers")
        return render(request,"Home/add_new.html",{})

    except HTTPException as e:
        logger.debug(f'{e}')
        raise e


def edit(request,id):
    try:
        if request.method == "POST":
            customer_name = request.POST['customer_name']
            email = request.POST['email']
            phone_number = request.POST['phone number']
            password = request.POST['password']
            city = request.POST['city']

            new_customer = CUSTOMER_INFO(customer_name = customer_name ,email_id= email,phone_number = phone_number,password= password, city=city, created_time= str(datetime.now()))
            new_customer.upd
            return redirect("all_customers")
        with connection.cursor() as cursor:
            cursor.execute(f"select * from django_app_customer_info where id={id}")
            result = cursor.fetchall()
            logger.debug(result)
        return render(request, "Home/update.html" , context={"customer":result})
    
    except HTTPException as e:
        logger.debug(f'{e}')
        raise e
    
def delete(request,id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"delete from django_app_customer_info where id={id}")
        return redirect("all_customers")
        
        

    except HTTPException as e:
        logger.debug(f'{e}')
        raise e

