# -*- coding: utf-8 -*-


from apps.env_setting.models import envinfo, rfrecord


def testdb_get(Nametmp):
    response = envinfo.objects.filter(Name=Nametmp)
    return response


def testdb_all():
    response = envinfo.objects.all()
    return response


def testdb_delete(Nametmp):
    response = envinfo.objects.get(Name=Nametmp).delete()
    return response


def testauto_get(IDtmp):
    response = rfrecord.objects.filter(ID=IDtmp)
    return response


def testauto_all():
    response = rfrecord.objects.all()
    return response


def testauto_delete(idtmp):
    response = rfrecord.objects.get(ID=idtmp).delete()
    return response


def testauto_last():
    response = rfrecord.objects.last()
    return response

def testauto_update(IDtmp, testtime):
    response = rfrecord.objects.filter(ID=IDtmp).update(TestTime=testtime)
    return response
