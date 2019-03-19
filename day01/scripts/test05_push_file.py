"""
    目标：使用appium内方法将文件推送到手机
"""
# 导包
from appium import webdriver
from time import sleep
import base64

# 前置代码、
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 需求：test08.txt发送到手机

# with open("./test08.txt", "r", encoding="utf-8") as f:
#     data = str(base64.b64encode(f.read().encode("utf-8")), "utf-8")
#     driver.push_file("/sdcard/test08.txt", data)





# 暂停3秒

# 将文件已b64位 推送到手机

# with open("./test08.txt", "r", encoding="utf-8") as f:
#     data = str(base64.b64encode(f.read().encode("utf-8")), "utf-8")
#     driver.push_file("/sdcard/test09.txt", data)

"""
    b64encode：加密
    b64decode: 解密
"""


# 从手机内获取test08.txt 到本地文件 test01.txt
data = driver.pull_file("/sdcard/test08.txt")
with open("./test01.txt", "w", encoding="utf-8") as f:
    f.write(str(base64.b64decode(data), "utf-8"))

sleep(3)

# 关闭所有
driver.quit()

