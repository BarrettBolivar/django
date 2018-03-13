# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    request.session['counter'] = 1
    context = {
    "random": get_random_string(length=14)
    }
    return render(request,'word_gen/index.html', context)
def create(request):
    context = {
    "random": get_random_string(length=14)
    }
    request.session['counter'] += 1
    return render(request,'word_gen/index.html', context)