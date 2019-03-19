"""
    目标：获取当前屏幕页面元素   结构
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

# 需求：启动设置界面，获取当前页面内所有元素

# 调用获取页面元素 结构方法
print(driver.page_source)

sleep(3)

# 关闭所有
driver.quit()

