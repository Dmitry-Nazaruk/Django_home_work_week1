from django.urls import path

from firstapp.views import hellodjango, date_url, date_year_url, date_month_url, date_day_url, helloname

urlpatterns = [
    path('', hellodjango),
    path('date/', date_url),
    path('date/year/', date_year_url),
    path('date/month/', date_month_url),
    path('date/day/', date_day_url),
    path('<str:name>/', helloname)
]