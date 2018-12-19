import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "18621512301@163.com"                  # 用户名
mail_pass = "1wonderful"               # 授权密码，非登录密码

sender = '18621512301@163.com'    # 发件人邮箱(最好写全, 不然会失败)


content = '''测试已完成，结果请查看
        http://192.168.133.29:8081/devops/result/'''

title = '自动化测试'  # 邮件主题

def sendEmail(address):
    receivers = address
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


