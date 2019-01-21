import time
import threading
import json
import re
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
#伪装浏览器
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

#获取网页源码
def get_one_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            #print('Web page request succeed.')
            return response
        return None
    except RequestException as e:
        print('网络错误')
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html, "lxml")
    content = soup.find('div','kspb-content')
    kyys = content('li' ,"kyy")
    
    empty = []
    now_time = time.strftime('%Y-%m-%d %X',time.localtime())
    if kyys == empty:
        print('now:' + now_time + 'status:无号')
    else:
        print('-----------------------------------------------------------')
        for kyy in kyys:
            string = str(kyy)
            fee = kyy['ghf']
            date = kyy['order_date']
            temp1_count = re.search(r'>(.*?)<br/>预约</li>',string,re.M)
            if temp1_count:
               temp2_count = temp1_count.group(0)
            final3_count = re.search(r'\d\d|\d',temp2_count,re.M)
            if final3_count:
                count = final3_count.group(0)
            #print(count)
            #print('now:'+ now_time +'有号日期：'+ date +'挂号费：'+fee)
            hospital_result = 'now:'+ now_time +'有号日期：'+ date + '剩余号数：'+ count
            print(hospital_result)
            with open('book_hospital_result.txt', 'a', encoding='utf-8') as f:
                f.write(json.dumps(hospital_result, ensure_ascii=False) + '\n')
                f.close()

def main():
    url = 'https://guahao.zjol.com.cn/pb/957108?deptId=7195&fuzzy_deptId=0&docId=&fuzzy_docId=0'
    #url = 'https://guahao.zjol.com.cn/pb/957108?deptId=5969&fuzzy_deptId=0&docId=&fuzzy_docId=0'
    html = get_one_page(url)
    if html == None:
        pass
    else:
        parse_one_page(html.text)

#定时执行任务
def timer_1():
    main()
    timer = threading.Timer(45,timer_1)
    timer.start()
    
#主函数    
if __name__ == '__main__':
    timer_1()
        

       

    
    
