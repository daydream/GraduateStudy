""" 
@version: v1.0 
@author: shadow 
@software: PyCharm 
@time: 2021/7/1 23:07 
"""

import requests
import time

headers = {"Referer": "https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}
postData = {"action": "login",
            "username": "***",  # 你的学号
            "password": "***",  # 你的密码
            "ac_id": "1",
            "user_ip": "",
            "nas_ip": "",
            "user_mac": "",
            "save_me": "0",
            "ajax": "1"}


# 判断登录状态
def isloginok():
    response_login = requests.get(r"https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&", headers=headers)
    if response_login.headers['Content-Length'] == str(7779):  # 7757
        return 1
    else:
        login = requests.post(r"https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&", headers=headers, data=postData)
        login.raise_for_status()  # 响应状态
        return 2


# 判断网络状态
def isnetok(url):
    try:
        res = requests.get(url, timeout=2)
        if res.status_code == 200:
            return 1
        else:
            return 2
    except:
        return 3


# 输出网络连接日志 
def lognetstatus(url):
    with open("log.txt", "a") as f:
        date_time = time.strftime("%Y-%m-%d, %H:%M:%S")
        f.write(date_time + "\n")
        net = isnetok(url)
        if net == 1:
            netstr = "网络状态正常，在线"
        else:
            login = isloginok()
            if net == 2 and login == 1:
                netstr = "网络状态异常，在线"
            elif net == 3 and login == 2:
                netstr = "无网络，已重连"
            else:
                netstr = "网络状态异常，已重连"
        f.write(netstr + "\n")


while True:
    lognetstatus(r"https://www.baidu.com/")
    time.sleep(30)
