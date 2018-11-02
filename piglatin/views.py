from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
    return render(req, 'hello.html')

def translate(req):
    return HttpResponse("This is the translate page.")