from django.shortcuts import render
from django.urls import path

def home(request):
    return HttpResponse("hola mundo")

def room(request):
    return HttpResponse("hola room")