from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())


def login(request):
    return HttpResponse("login suceessfully!!")