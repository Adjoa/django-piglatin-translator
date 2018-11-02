from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
    # return HttpResponse("Hello, world!")
    return render(req, 'hello.html')