# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .backend import robot_exec
from . import change_config
import os
import time
import sys



sys.path.append("../")
from env_setting.env_CRUD import *


def exec(request):
    ctx = {}
    showlog = []
    with open('/root/mygithub/caiman/robotgogo/robotexec.log') as f:
        logtmp = f.readlines()
    logttt = logtmp[-10:]
    ctx['li'] = logttt
    return render(request, 'exec_test_UI.html', ctx)




def UI_test(request):
    ctx = {}
    result = testdb_all(request)

    ctx['li'] = result
    if request.POST:
        ctx['rln'] = request.POST['nn']
        testmodel = request.POST['mm']
        ctx['ccc'] = 'devops'
        Nametmp = request.POST['nn']
        tmpdata = testdb_get(request, Nametmp)
        IPtmp = tmpdata[0].IP
        registrytmp = tmpdata[0].Registry
        change_config.change_config_IP(IPtmp)
        change_config.change_config_registry(registrytmp)
        singalend = robot_exec.runRobot(testmodel)
        for i in range(10):
            time.sleep(5)
            if singalend == 0:
                backWord = 'doing'
                ctx['rlt'] = backWord
                return render(request, "setconfig_UI.html", ctx)
            else:
                ctx['rlt'] = 'done'
                return render(request, "setconfig_UI.html", ctx)
    return render(request, "setconfig_UI.html", ctx)


