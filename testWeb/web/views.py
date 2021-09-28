from django.shortcuts import render, HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    context = {
        'author': 'Dhruvin',
        'date': '11-04-2021'
    }
    return render(request, 'about.html', context)


def services(request):
    return HttpResponse('This is services page')
