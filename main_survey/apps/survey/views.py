from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'survey/index.html')

def create(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    context = {
        "name": request.POST['name'],
        "location": request.POST['location'],
        "language": request.POST['language'],
        "comment": request.POST['comment']
    }
    global context
    return redirect('survey/result')

def result(request):
    return render(request,'survey/result.html', context)

def returned(request):
    return render(request, 'survey/index.html')