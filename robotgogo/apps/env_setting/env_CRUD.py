# -*- coding: utf-8 -*-
 

 
from .models import envinfo

def testdb_get(request, Nametmp):
    response = envinfo.objects.filter(Name=Nametmp)
    return response


def testdb_all(request):
    response = envinfo.objects.all()
    return response


def testdb_delete(request,Nametmp):
    response = envinfo.objects.get(Name=Nametmp).delete()
    return response
