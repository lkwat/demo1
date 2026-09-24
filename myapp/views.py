from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bweb(request):
    return HttpResponse("Hello, this is the home page.完成")
def aweb(request):
    return HttpResponse("Hello, this is the aweb.")
