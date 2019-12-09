from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time


def home(request):
    return HttpResponse('Greetings. Welcome to the time machine.')


def today(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))


def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
