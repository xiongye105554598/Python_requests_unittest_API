# _*_ coding:utf-8 _*_
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail(file_new):
    """定义发送邮件函数"""
    mail_from='xiongye105554598@126.com'                              #发信邮箱
    mail_to=['jun.xiong@cdskysoft.com']   #收信邮箱
    f = open(file_new, 'rb')                                  #打开文件
    mail_body = f.read()                                      #读取文件
    f.close()                                                 #关闭文件
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')  #内容、格式、编码
    msg['From'] = "{}".format(mail_from)                      #发件人
    msg['To'] = ";".join(mail_to)                              #收件人
    msg['Subject']="API自动化测试报告"                  #邮件主题
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')     #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间

    smtp=smtplib.SMTP()
    #smtp.set_debuglevel(1)                                    # 开启发送debug模式，把发送邮件的过程显示出来
    smtp.connect('smtp.126.com',25)                               #设置第三方SMTP服务器
    #smtp.starttls()                                           # 启动安全传输模式
    smtp.login('xiongye105554598@126.com','JJBSMQQDYWYEIZXN')         #用户名、#授权密码，非登录密码
    smtp.sendmail(mail_from,mail_to,msg.as_string())          #配置发送邮箱，接收邮箱，以及发送内容
    smtp.quit()                                               #关闭发邮件服务
#


def send_mail(title, message, receiver, attach_file=''):

    # python3.7版本开始，在SMTP建立阶段就要指明host地址，3.7之前不需要
    smtp = smtplib.SMTP(host='smtp.qq.com')
    smtp.connect(host='smtp.qq.com', port=25)    # 建立连接
    smtp.starttls()                        # 网站需要安全认证时添加
    smtp.login('xxxxxx@qq.com','xxxxxx')         #用户名、#授权密码，非登录密码
    msg = MIMEMultipart()
    content = MIMEText(message, 'html', 'utf-8')
    msg['Subject'] = f'{title}'
    msg['From'] = 'sender'
    msg['To'] = receiver
    msg.attach(content)

    if attach_file:
        att1 = MIMEText(open(attach_file, 'rb').read(), 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment; filename="report.txt"'
        msg.attach(att1)

    try:
        smtp.send_message(msg)
        status = 'Success'
        print(status)
    except smtplib.SMTPException as e:
        print(e)
        status = 'Failed'

    smtp.quit()
    return status


if __name__ == '__main__':
    file=r'E:\Python\案例\接口自动化测试案例\Report\API自动化测试报告20200716133110.html'
    send_mail('title', 'msg', '105554598@163.com',r'E:\Python\案例\接口自动化测试案例\Report\API自动化测试报告20200716164242.html')
