def get_log(request):
    ctx = {}
    ctx['rln'] = 'kkk'
    with open('/root/mygithub/caicloudQA/robotgogo/robot.log') as f:
        logtmp = f.readlines()
    logttt = logtmp[-10:]
    ctx['li'] = logttt
    return render(request, 'exec_test.html',  ctx)