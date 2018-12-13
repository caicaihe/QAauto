# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):

    return render(request, 'base.html')

def run_test(request):

    return render(request, 'run_test.html')