from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def translate(req):
    return HttpResponse("This is the translate page. " + req.GET['original_text'])