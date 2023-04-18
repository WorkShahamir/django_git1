from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('index')


def about(request):
    return HttpResponse('about')


