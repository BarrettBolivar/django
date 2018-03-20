# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from datetime import datetime
import random

def index(request):
    return HttpResponse('placeholder to display all the surveys created')

def new(request):
    return HttpResponse('placeholder for users to add a new survey')
