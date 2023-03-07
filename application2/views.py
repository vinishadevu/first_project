from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vinisha(request):
    return HttpResponse('<h1>vinisha is a good girl</h1>')
