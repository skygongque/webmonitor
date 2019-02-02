import time
import json
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

headers = {
    'Cookie': 'IjIR_2132_saltkey=F2TEk0Np; IjIR_2132_lastvisit=1547783388; IjIR_2132_sendmail=1; Hm_lvt_7e0a8cd31f216218c3ab717f5413612b=1547215569,1547786991; IjIR_2132_con_request_uri=http%3A%2F%2Fwww.pan6.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dindex.php%253Ftn%253D02049043_62_pg; IjIR_2132_sid=DVPp6S; IjIR_2132_client_created=1547786999; IjIR_2132_client_token=59760589B75F85755C4C6E2BA0B7C01C; IjIR_2132_ulastactivity=7a60cC0Tf71h2H2ebhBbo1PC0uxg%2FynhV1og%2FaktWY95aS7XcDGs; IjIR_2132_auth=37b5StXsUDRd3lpgr97iRHUxXq6CnjbM8yna25XSNrVjJCYBlASqsOYReaqnCH71c82JOe6%2F7%2FUCuhK%2FGhbb%2B0fRsew; IjIR_2132_connect_login=1; IjIR_2132_connect_is_bind=1; IjIR_2132_connect_uin=59760589B75F85755C4C6E2BA0B7C01C; IjIR_2132_stats_qc_login=3; IjIR_2132_dsu_amupper=DQo8c3R5bGU%2BDQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU%2BDQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCg0KPHN0cm9uZz7ntK%2ForqHnrb7liLA8c3BhbiBjbGFzcz0idGltZXMiPjI2ODwvc3Bhbj7mrKE8L3N0cm9uZz48YnI%2BDQoNCjxBIEhSRUY9ImZvcnVtLnBocD9tb2Q9dmlld3RocmVhZCZhbXA7dGlkPTE4MDgzNyZhbXA7YXV0aG9yaWQ9MzA3NDI5IiB0YXJnZXQ9Il9ibGFuayI%2B5p%2Bl55yL562%2B5Yiw5Zue5biWPC9BPg0KDQo8c3Ryb25nPui%2Fnue7reetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI%2BNDwvc3Bhbj7mrKE8L3N0cm9uZz48YnI%2BDQoNCjxzdHJvbmc%2B5LiK5qyh562%2B5YiwOiA8c3BhbiBjbGFzcz0idGltZXMiPjIwMTktMDEtMTcgMTE6MjI6MjI8L3NwYW4%2BPC9zdHJvbmc%2BDQo8L2Rpdj4NCg%3D%3D; IjIR_2132_nofavfid=1; IjIR_2132_study_nge_extstyle=auto; IjIR_2132_study_nge_extstyle_default=auto; Hm_lpvt_7e0a8cd31f216218c3ab717f5413612b=1547787015; IjIR_2132_lastact=1547787015%09plugin.php%09',
    'Host': 'www.pan6.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }


def get_one_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            print('resquest succeed!')
            return response
        return None
    except RequestException as e:
        print(e)
        return None


def parse_one_page(html):    
    soup = BeautifulSoup(html, "lxml")
    ppra = soup.select('#pper_a')[0]['href']
    base = 'http://www.pan6.com/'
    link = base + ppra
    return link
'''
def get_score(html):    
    soup = BeautifulSoup(html, "lxml")
    score = soup.select('#psts > ul > li')[3]
    score_text =  score.text
    #print(score_text)
'''    


def mark(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            print('mark succeed or marked')
            return response
        return None
    except RequestException as e:
        input(e)
        return None


def main():
    url = 'http://www.pan6.com/'
    html = get_one_page(url)
    link = parse_one_page(html.text)
    time.sleep(1)
    mark(link)
    '''
    time.sleep(1)
    my_url = 'http://www.pan6.com/space-uid-307429.html'
    score_html = get_one_page(my_url)
    get_score(score_html.text)
    '''
    
        
   
if __name__ == '__main__':
    while True:
        main()
        time.sleep(14400)
        

       

