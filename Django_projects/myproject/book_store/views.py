from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("Welcome to my book store.")

#Use the Django ORM to create, retrieve, update, and delete Product instances.



