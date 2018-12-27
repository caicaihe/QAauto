import os
import sys
import datetime

from apps.env_setting.env_CRUD import *
from backend.change_config import *


def run_robot(rfrecordID):
    bb = testauto_get(rfrecordID)
    rfrecordName = bb[0].Name
    testModel = bb[0].TestModel
    envNametmp = bb[0].envName
    change_env(envNametmp)
    print(testModel)
    robotScrptDir = "/root/mygithub/quality/automation/rf/compass/devops/测试用例/API/"+testModel+"API.txt"
    now = datetime.datetime.now().strftime('%Y%m%d%H%M')
    testauto_update(rfrecordID, now)
    resultDir = "/opt/rfresult/"+rfrecordName+'/'+now
    command = "robot --outputdir"+"  "+resultDir+" "+robotScrptDir
    print(command)
    output = os.system(command)
    if output:
        return 1




