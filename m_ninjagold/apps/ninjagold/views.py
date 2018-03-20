# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from datetime import datetime
import random

def index(request):
    request.session['log'] = []
    request.session['state'] = None
    request.session['time'] = None
    request.session['gold'] = 0
    request.session['delta'] = 0
    request.session['building']= None
    return render(request, 'ninjagold/index.html')

def pick(request):
    request.session['state'] = 'process_money'
    if request.POST['building'] == 'farm':
        request.session['delta'] = random.randint(10,20)
        request.session['gold'] += request.session['delta']
        request.session['building'] = 'farm'
    elif request.POST['building'] == 'cave':
        request.session['delta'] = random.randint(5,10)
        request.session['gold'] += request.session['delta']
        request.session['building'] = 'cave'
    elif request.POST['building'] == 'house':
        request.session['delta'] = random.randint(2,5)
        request.session['gold'] += request.session['delta']
        request.session['building'] = 'house'
    elif request.POST['building'] == 'casino':
        request.session['delta'] = random.randint(-50,50)
        request.session['gold'] += request.session['delta']
        request.session['building'] = 'casino'
    request.session['time'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    request.session['log'].append((request.session['building'],request.session['delta'],request.session['time']))
    return render(request, 'ninjagold/index.html')

def reset(request):
    request.request.session.clear()
    return render(request, 'ninjagold/index.html')
