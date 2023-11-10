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
    return render(request, "Home/index.html", context={"peoples": peoples})


def login(request):
    return render(request, "Home/index.html")
    # return HttpResponse("login suceessfully!!")
