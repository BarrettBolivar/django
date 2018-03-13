# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
  context = {
  "random": get_random_string(length=14)
  }
  return render(request,'timeDisplay/index.html', context)
# Create your views here.
