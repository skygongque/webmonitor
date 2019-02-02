import time
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.qq.com" 
mail_user = "1243650225"  
mail_pass =  
 
sender = '1243650225@qq.com'  
receivers = ['1243650225@qq.com'] 

content = '有号' 
title = '有号提醒' 


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

def send_email():
    message = MIMEText(content, 'plain', 'utf-8')  
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.login(mail_user, mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("email send successful!")
    except smtplib.SMTPException as e:
        print(e)

def get_one_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            print('resquset succeed!')
            return response.text
        return None
    except RequestException as e:
        print(e)
        return None

def parse_one_page(html):    
    soup = BeautifulSoup(html, "lxml")
    kyy = soup.select('li.kyy')
    empty = []
    if kyy == empty:
        print('empty!')
    else:
        print('matched!')
        send_email()
    


def main():
    #url = 'https://guahao.zjol.com.cn/pb/957108?deptId=7195&fuzzy_deptId=0&docId=&fuzzy_docId=0'
    url = 'https://guahao.zjol.com.cn/pb/957108?deptId=5969&fuzzy_deptId=0&docId=&fuzzy_docId=0'
    html = get_one_page(url)
    parse_one_page(html)
    
      
if __name__ == '__main__':
    while True:
        main()
        time.sleep(60)
        

       

    
    
