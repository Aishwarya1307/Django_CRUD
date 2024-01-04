from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection
import json

def home(request):
    return render(request, "Home/Home.html")


def customer(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from Customer_details")
        context =  cursor.fetchone()
        print(context)
    return render(request, "Home/all_customers.html" , context={"customers": context})


def add_new(request):
    return render(request,"Home/add_new.html")
