from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from datetime import datetime
import random

def index(request):
    return HttpResponse('no connection yet')

def register(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')

def user(request):
    return HttpResponse('placeholder to later display all the list of users')