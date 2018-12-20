import os
import sys
import datetime

sys.path.append("../")
from env_setting.env_CRUD import *


def  runRobot(rfrecordName):
    print(rfrecordName)
    bb = testauto_get(rfrecordName)
    testModel = bb[0].TestModel
    print(testModel)
    robotScrptDir = "/root/mygithub/quality/automation/rf/compass/devops/测试用例/API/"+testModel+"API.txt"
    now=datetime.datetime.now().strftime('%Y%m%d%H%M')
    testauto_update(rfrecordName, now)
    resultDir = "/opt/rfresult/"+rfrecordName+'/'+now
    command = "robot --outputdir"+"  "+resultDir+" "+robotScrptDir
    print(command)
    output = os.system(command)
    if output:
        return 1




    
