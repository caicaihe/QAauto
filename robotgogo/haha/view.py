# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.shortcuts import render
from backend import robot_exec, send_email
from apps.env_setting.env_CRUD import *


def hello(request):
    return render(request, 'base.html')


def run_test(request):
    return render(request, 'run_test.html')


def webhook(request):
    if request.method == 'POST':
        infotmp = request.body
        json_data = json.loads(infotmp)
        if json_data['status'] == "Success":
            res = testauto_last()
            rfrecordName = res.Name
            robot_exec.run_robot(rfrecordName)
            emailtmp = res.email1
            address_list = [emailtmp]
            send_email.sendEmail(address_list, rfrecordName)
            return HttpResponse(emailtmp)

        else:
            return HttpResponse('letsout')
    return HttpResponse('HAHAWAWA')

