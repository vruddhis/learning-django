from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse


def index(request):
    return HttpResponse("Hi this is a wordle game!")