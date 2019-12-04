import userAgent
import requests
import random
import time



def get_info():

  headers = {
    'Host': 'securelogin.arubanetworks.com',
    'Connection': 'keep-alive',
    'Content-Length': '189',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ayxy.pheicloud.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': f'{userAgent.get_userAgent()}',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ayxy.pheicloud.com/Portal/Portal/arubapass?url=http%3A%2F%2Fayxy.pheicloud.com%2FHome%2FMenu%2FtoPay%3Fmac%3D4c49e3434e30%26menu_id%3D50%26type%3D1%26num%3D1&username=tmpuser&password=tmpuser',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.9',
        }
  return headers

data = {
  'user': 'tmpuser',
  'password': 'tmpuser',
  'cmd': 'authenticate',
  'mac': '',
  'ip': '',
  'essid': '',
  'url': 'http://ayxy.pheicloud.com/Home/Menu/toPay?mac=4c49e3434e30&menu_id=50&type=1&num=1',
  'Login': 'login'
        }




#获取 分和秒
def get_date():
    return time.localtime()[4],time.localtime()[5]

#获取与 get_data()函数 时间差
def get_dates(m,s):
    mm,ss = get_date()

    print(f'\033[0;33;31m [结束时间]\033[0m：{time.localtime()[3]}小时 {mm}分钟 {ss}秒\n')

    mm = mm-m
    if mm == 0:
        time_s = ss-s
    if mm == 1:
        time_s1  = 60-s
        time_s   = ss + time_s1
    if mm >=2:
        time_s1 = (60-s)+ss

        mm -= 1
        time_s2 = mm*60

        time_s = time_s1 + time_s2
    return time_s


def getNetwork():
  requests.post('http://securelogin.arubanetworks.com/cgi-bin/login', headers=get_info(), data=data)
  print('\t\033[1;33;33m [Info]\033[0m: Get success')


#获取网络 !!!
def get_network():
    m,s = get_date()
    print(f'\033[0;33;31m [开始时间]\033[0m： {time.localtime()[3]}小时 {m}分钟 {s}秒')

    getNetwork()

    sub = int(get_dates(m,s))
    
    times = 185
    if sub >=times:
        sub = 0
    if sub <=times:
        sub = times-sub
    
    for x in range(sub,-1,-1):
        mystr = f"\033[1;35;32m 网络\033[0m--{sub}s/" + str(x) + "s-- 后会重新刷新"
        print(mystr,end = "")
        print("\b" * (len(mystr)*2),end = "",flush=True)
        time.sleep(1)


def main():
    print('\033[0;45m 安阳学院互联网获取..... \033[0m')
    get_network()
    while True:
        print('\033[0;35;46m 网络获取刷新中....... \033[0m')
        get_network()



main()
















