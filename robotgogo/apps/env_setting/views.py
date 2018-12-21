# -*- coding: utf-8 -*-


from django.shortcuts import render

from apps.env_setting.env_CRUD import *


# 表单
def base(request):
    return render(request, "env_base.html")

def env_auto(request):
    result = testauto_all()
    if request.POST:
        Nametmp = request.POST['nm']
        envNametmp = request.POST['nn']
        TestModeltmp = request.POST['mm']
        email1tmp1 = request.POST['nn1']
        email1tmp2 = request.POST['nn2']
        email1tmp3 = request.POST['nn3']
        test1 = rfrecord(Name=Nametmp, envName=envNametmp, TestModel=TestModeltmp, email1=email1tmp1, email2=email1tmp2, email3=email1tmp3, autopush=True)
        test1.save()
        result2 = testauto_get(Nametmp)
        return render(request, "setconfig_auto.html", {'li2': result2})
    return render(request, "setconfig_auto.html", {'li2': result})


def env_setting(request):
    result = testdb_all()
    return render(request, "env_setting.html", {'li': result})


def env_add(request):
    ctx = {}
    result = testdb_all()
    if request.POST:
        Nametmp = request.POST['n']
        IPtmp = request.POST['q']
        Registrytmp = request.POST['r']
        test1 = envinfo(Name=Nametmp, IP=IPtmp, Registry=Registrytmp)
        test1.save()
    return render(request, "env_setting.html", {'li': result})


def env_delete(request):
    ctx = {}
    result = testdb_all()
    if request.POST:
        Nametmp_del = request.POST['nd']
        testdb_delete(Nametmp_del)
    return render(request, "env_setting.html", {'li': result})


def envauto_add(request):
    ctx = {}
    result = testdb_all()
    if request.POST:
        Nametmp = request.POST['nn']
        rrlist = testauto_get(Nametmp)
        IPtmp = rrlist[0].IP
        Registrytmp = rrlist[0].Registry
        TestModeltmp = request.POST['mm']
        email1tmp1 = request.POST['nn1']
        email1tmp2 = request.POST['nn2']
        email1tmp3 = request.POST['nn3']
        test1 = rfrecord(Name=Nametmp, IP=IPtmp, Registry=Registrytmp, TestModel=TestModeltmp, email1=email1tmp1, email2=email1tmp2, email3=email1tmp3)
        test1.save()
        result2 = testauto_all()
        return render(request, "setconfig_auto.html", {'items2': result2})
    return render(request, "setconfig_auto.html", {'li': result})


def envauto_delete(request):
    ctx = {}
    result = testdb_all()
    if request.POST:
        Nametmp_del = request.POST['nd']
        testdb_delete(Nametmp_del)
    return render(request, "env_setting.html", {'li': result})

