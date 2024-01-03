from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    peoples = [
        {'name': 'Abhijeet', 'age': 26},
        {'name': 'Ajinkya', 'age': 24},
        {'name': 'Riya', 'age': 17},
        {'name': 'aryan', 'age': 30},
        {'name': 'john', 'age': 18},
        {'name': 'kavya', 'age': 20},
    ]
    return render(request, "Home/Home.html", context={"peoples": peoples})


def customer(request):
    return render(request, "Home/all_customers.html")
    # return HttpResponse("login suceessfully!!")


def add_new(request):
    return render(request,"Home/add_new.html")
