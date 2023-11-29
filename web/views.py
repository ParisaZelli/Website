from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'site/index.html')


def about(request):
    return render(request,'site/about.html')


def contact(request):
    return render(request,'site/contact.html')

def test(request):
    return render(request,'site/test.html')

