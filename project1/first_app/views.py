from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse("This is home page from first_app")
def contact(req):
    return HttpResponse("This is contact page from first_app")
