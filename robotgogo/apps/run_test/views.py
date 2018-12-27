# -*- coding: utf-8 -*-

from django.shortcuts import render
from backend import robot_exec
from backend import change_config
from backend import send_email

import time

from apps.env_setting.env_CRUD import *


def exec(request):
    ctx = {}
    showlog = []
    with open('/root/mygithub/caiman/robotgogo/robotexec.log') as f:
        logtmp = f.readlines()
    logttt = logtmp[-10:]
    ctx['li'] = logttt
    return render(request, 'exec_test.html', ctx)




def run_test(request):
    ctx = {}
    result = testauto_all()
    ctx['li'] = result
    if request.POST:
        IDtmp = request.POST['nn']
        tmpdata = testauto_get(IDtmp)
        TestNametmp = tmpdata[0].Name
        envNametmp = tmpdata[0].envName
        envtmpdata = testdb_get(envNametmp)
        IPtmp = envtmpdata[0].IP
        registrytmp = envtmpdata[0].Registry
        change_config.change_config_IP(IPtmp)
        change_config.change_config_registry(registrytmp)
        singalend = robot_exec.run_robot(IDtmp)
        tmpdata2 = testauto_get(IDtmp)
        TestTime = tmpdata2[0].TestTime
        send_email.sendEmail(IDtmp)
        for i in range(10):
            time.sleep(5)
            if singalend == 0:
                backWord = 'doing'
                ctx['rlt'] = backWord
                return render(request, "set_test.html", ctx)
            else:
                ctx['rlt'] = 'done'
                ctx['link'] = "http://192.168.133.29:8081/" + TestNametmp + "/" + TestTime + "/"
                return render(request, "set_test.html", ctx)
    return render(request, "set_test.html", ctx)


