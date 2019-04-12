# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My 2nd Pro</em>")
def help(request):
    helpdict = { 'help_insert':'HELP PAGE'}
    return render(request,'help.html',context=helpdict)
    

# Create your views here.
