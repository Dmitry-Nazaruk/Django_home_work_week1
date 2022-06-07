from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello django")


def helloname(request: HttpRequest, name: str):
    return HttpResponse(f"Hello {name}")

def date_url(request: HttpRequest):
    return HttpResponse("22.03.2022")

def date_year_url(request: HttpRequest):
    return HttpResponse("22")

def date_month_url(request: HttpRequest):
    return HttpResponse("03")