from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from models import *

def index(request):
    user = User.objects.all()
    print user
    return render(request, 'semi_restful/index.html', {"user":user})

def new_user(request):
    return render(request, 'semi_restful/new.html')

def show(request, id):
    user = User.objects.get(id=id)
    return render(request, 'semi_restful/show.html', {"user" : user})

def editpage(request, id):
    User.objects.get(id=id)
    return redirect(request, 'edit/')

def edit(request, id):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+id)
    else:
        users = User.objects.get(id = id)
        users.name = request.POST['name']
        users.desc = request.POST['desc']
        users.save()
        return redirect('/')


def destroy(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect('/')

def create(request):
    su = User.objects.create(name=request.POST['full_name'], email = request.POST['email'])
    su.save()
    return redirect('/')