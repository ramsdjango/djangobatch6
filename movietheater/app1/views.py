# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def movietheater(request):
	return render(request,"app1/index.html")

def people(request):
	return render(request,"app1/index.html")

def enquiry(request):
	return render(request,"app1/index.html")

