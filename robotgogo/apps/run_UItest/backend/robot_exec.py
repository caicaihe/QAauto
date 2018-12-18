import os



def  runRobot(testModel):
    robotScrptDir = "/root/mygithub/quality/automation/rf/compass/devops/测试用例/UI/UItest.txt"
    resultDir = "/opt/rfresult/devops/result"
    #command = "nohup"+" "+"robot --outputdir"+"  "+resultDir+" "+robotScrptDir+" "+">robotexec.log"
    command ="robot --outputdir" + "  " + resultDir + " " + robotScrptDir+" "+">robotexec.log"
    print(command)
    os.system(command)




