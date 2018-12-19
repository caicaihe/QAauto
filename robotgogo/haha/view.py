# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.shortcuts import render
from .backend import send_email, robotExec

 
def hello(request):

    return render(request, 'base.html')

def run_test(request):

    return render(request, 'run_test.html')

def webhook(request):
    if request.method == 'POST':
        infotmp = request.body
        json_data = json.loads(infotmp)
        if json_data['status'] == "Success":
            robotExec.runRobot("devops")
            address_list = ["zhujian@caicloud.io", "heliping_peter@outlook.com"]
            send_email.sendEmail(address_list)
            return HttpResponse('letsgo')

        else:
            return HttpResponse('letsout')
    return HttpResponse('HAHAWAWA')
