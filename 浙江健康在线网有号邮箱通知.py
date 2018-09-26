#计时器引用的库
import threading
import time
#获取网站源码引用库
import urllib.request
#发邮件引用的库
import smtplib
from email.mime.text import MIMEText
 
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # SMTP服务器
mail_user = "12*****225"  # 用户名
mail_pass = "********"  # 授权码
 
sender = '12*****225@qq.com'  # 发件人邮箱
receivers = ['12******225@qq.com']  # 接收人邮箱

content = '有号提醒' 
title = '有号提醒' # 邮件主题

message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

#定义一个获取网站源码的函数
def grab(url):
    # 打开传入的网址
    resp = urllib.request.urlopen(url)
    # 读取网页源码内容
    dat = resp .read()
    data=dat.decode("utf-8").encode("gbk")
    # 输入存储文件名
    name = "baya.txt"
    # 打开文件
    file_name = open(name, "wb")
    # 将代码写入文件
    file_name.write(data)
    # 关闭文件
    file_name.close()
    print("下载源码完成")

#判断TXT文件中是否有指定字符，如果有发邮件提醒有号
def xf(files,string):
    
    with open(files) as e:
        if e.read().find(string)==-1:
            print("没有号")
            
        else:
            print("有号,正在发送邮件。。。。")
            try:
                smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
                smtpObj.login(mail_user, mail_pass)  # 登录验证
                smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
                print("邮件发送成功")
            except smtplib.SMTPException as e:
                print(e)

#main
if __name__ == '__main__':
    # 按照格式输入网址
    def fun_timer():
        print("=============================================")
        web_addr = "http://guahao.zjol.com.cn/pb/957108?deptId=7195&fuzzy_deptId=0&docId=&fuzzy_docId=0"
        try:
            grab(web_addr)
            xf('C:/Users/Administrator/Desktop/baya.txt','<br />预约</li>')
        except:
            print("网络错误")
        global timer
        #重复构造定时器
        timer = threading.Timer(45,fun_timer)
        timer.start()
    #定时调度
    timer = threading.Timer(0,fun_timer)
    timer.start()
    

        
