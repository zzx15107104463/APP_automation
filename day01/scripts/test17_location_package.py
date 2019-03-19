
# 导包
from appium import webdriver
from time import sleep
import base64

# 前置代码、
# server 启动参数
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 解决中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

"""
    需求：
      1. 获取搜索按钮 在屏幕中间位置
      2. 获取当前设置app 的包名和启动名
"""
# 点击搜索按钮
# el = driver.find_element_by_id("com.android.settings:id/search")
# print(el.location)

# 获取启动名

print("包名：", driver.current_package)
# 获取包名
print("启动名：", driver.current_activity)


sleep(3)
driver.quit()








