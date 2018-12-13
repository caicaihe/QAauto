# -*- coding: utf-8 -*-

import os
import sys

sys.path.append("..")
from django.http import HttpResponse
from django.shortcuts import render

# from models import envinfo
from .models import envinfo
from .env_CRUD import *

import sys

sys.path.append("..")
from .env_CRUD import *


# 表单
def env_setting(request):
    ctx = {}
    result = testdb_all(request)
    return render(request, "env_setting.html", {'li': result})

def env_add(request):
    ctx = {}
    result = testdb_all(request)
    if request.POST:
        Nametmp = request.POST['n']
        IPtmp = request.POST['q']
        Registrytmp = request.POST['r']
        test1 = envinfo(Name=Nametmp, IP=IPtmp, Registry=Registrytmp)
        test1.save()
    return render(request, "env_setting.html", {'li': result})


def env_delete(request):
    ctx = {}
    result = testdb_all(request)
    if request.POST:
        Nametmp_del = request.POST['nd']
        testdb_delete(request, Nametmp_del)
    return render(request, "env_setting.html", {'li': result})
