from django.shortcuts import render

from django.http import HttpResponse as hr
# Create your views here.
def index(request):
    return hr("Hello, World. You're at the Polls index")

