import random
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def about_me(request):
    return render(request, 'generator/about_me.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPSADFGHJKLZXCVBVNM'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    lenght = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
