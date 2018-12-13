import os


def  runRobot(testModel):
    robotScrptDir = "/root/mygithub/quality/automation/rf/compass/devops/测试用例/API/"+testModel+"API.txt"
    resultDir = "/opt/rfresult/devops/result"
    command = "robot --outputdir"+"  "+resultDir+" "+robotScrptDir
    print(command)
    output = os.system(command)
    if output:
        return 1



    
