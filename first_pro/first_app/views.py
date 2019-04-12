# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict={'inset_me':"Hello I am from views.py"}
    return render(request,'index.html',context=my_dict)

# Create your views here.
