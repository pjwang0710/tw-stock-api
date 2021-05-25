from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())


def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())
