from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello django")


def helloname(request: HttpRequest, name: str):
    return HttpResponse(f"Hello {name}")


def date_url(request: HttpRequest):
    return HttpResponse(datetime.today().strftime('%d.%m.%Y'))


def date_year_url(request: HttpRequest):
    return HttpResponse(datetime.today().strftime('%Y'))


def date_month_url(request: HttpRequest):
    return HttpResponse(datetime.today().strftime('%m'))


def date_day_url(request: HttpRequest):
    return HttpResponse(datetime.today().strftime('%d'))
