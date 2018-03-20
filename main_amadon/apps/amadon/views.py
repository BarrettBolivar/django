# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'amadon/index.html')

def create(request):
    if 'ttotal' not in request.session:
        request.session['ttotal'] = 0.00
    if 'atotal' not in request.session:
        request.session['atotal'] = 0

    amount = request.POST['quantity']
    value = request.POST['product_id']
    total = 0
    print value
    if int(value) == 1015:
        total = float(amount) * 19.99
    elif int(value) == 1016:
        total = float(amount) * 29.99
    elif int(value) == 1017:
        total = float(amount) * 4.99
    elif int(value) == 1018:
        total = float(amount) * 49.99
    else:
        return HttpResponse('Nothing ordered')

    request.session['ttotal'] = total + request.session['ttotal']
    request.session['atotal'] = int(request.POST['quantity']) + int(request.session['atotal'])

    context = {
        "amount": request.POST['quantity'],
        "total": total,
        "ttotal": request.session['ttotal'],
        "atotal": request.session['atotal']
    }
    global context
    return redirect('amadon/result')

def result(request):
    return render(request,'amadon/checkout.html', context)

def returned(request):
    return render(request, 'amadon/index.html')

