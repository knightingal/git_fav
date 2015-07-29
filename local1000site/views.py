from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requeset):
    return HttpResponse("this is local1000/index")
