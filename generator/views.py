from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    # return HttpResponse("Hello world!")
    # return render(request, 'generator/home.html')
    return render(request, 'generator/home.html',)


def about(request):
    return render(request, 'generator/about.html',)


def password(request):

    characters = list('abcdefghijklmnopoqrstuvwwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 12))
    the_password = ''
    for x in range(lenght):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})
