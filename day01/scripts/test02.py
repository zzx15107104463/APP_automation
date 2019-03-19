"""
    目标：在应用中启动其他应用
    需求：
        1. 启动设置应用
        2. 3秒钟后启动短信应用
    方法：
         driver.start_activity(appPackage,appActivity)
"""
# 导包
from appium import webdriver
from time import sleep

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

# 暂停3秒
sleep(3)
# 关闭 设置
driver.close_app()

# 启动短信应用  com.android.mms/.ui.ConversationList
driver.start_activity("com.android.mms", ".ui.ConversationList")

# 关闭所有
driver.quit()  

