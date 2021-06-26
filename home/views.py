from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    text = "Django Kurulumu : Python -m pip install <br> Proje Oluşturma :Django-admin startproject mysite <br> App ekleme : Python manage.py starapp polls"
    context = {'text': text}
    return render(request, 'index.html', context)
