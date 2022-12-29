from django.shortcuts import render
from django.http import HttpResponse

def sunday(request):
    return HttpResponse('<h1>sunday is funday</h1>')

def rokesh(request):
    return HttpResponse('<h1>rockesh sir is my html trainer</h1>')
