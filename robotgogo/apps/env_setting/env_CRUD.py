# -*- coding: utf-8 -*-


from .models import envinfo, rfrecord


def testdb_get(Nametmp):
    response = envinfo.objects.filter(Name=Nametmp)
    return response


def testdb_all():
    response = envinfo.objects.all()
    return response


def testdb_delete(Nametmp):
    response = envinfo.objects.get(Name=Nametmp).delete()
    return response


def testauto_get(Nametmp):
    response = rfrecord.objects.filter(Name=Nametmp)
    return response


def testauto_all():
    response = rfrecord.objects.all()
    return response


def testauto_delete(idtmp):
    response = rfrecord.objects.get(id=idtmp).delete()
    return response


def testauto_last():
    response = rfrecord.objects.last()
    return response

def testauto_update(name, testtime):
    response = rfrecord.objects.filter(Name=name).update(TestTime=testtime)
    return response
