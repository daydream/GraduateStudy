""" 
@version: v1.0 
@author: shadow
@software: PyCharm
@time: 2021/5/4 20:51 
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True  # 无界面运行
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0')

while True:
    driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=options)
    driver.get('https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&is_second=1?url=www.msftconnecttest.com')
    time.sleep(5)

    try:
        username = driver.find_element_by_xpath("//table[@id='id_login']/tbody[1]/tr[2]/td[2]/input[1]")  # 通过xpath路径定位
        password = driver.find_element_by_xpath("//table[@id='id_login']/tbody[1]/tr[3]/td[2]/input[1]")
        login = driver.find_element_by_xpath("//table[@id='id_login']/tbody[1]/tr[4]/td[2]/p[1]/input[1]")

        # 键入数据，学号密码
        username.clear()
        username.send_keys('***')  # 你的学号
        password.clear()
        password.send_keys('***')  # 你的密码
        login.click()  # 登录
        driver.quit()   # 关闭浏览器
        print("登录成功")
    except:
        driver.quit()
        print("已登录")

    time.sleep(3600)     # 多长时间检查一次
