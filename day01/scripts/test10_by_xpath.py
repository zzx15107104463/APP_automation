
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

"""
  业务场景:
        1.进入设置页面
        2.点击WLAN菜单栏 (使用xpath)
"""

# 使用xpath定位 wlan并点击
# driver.find_element_by_xpath("//*[contains(@text,'LAN')]").click()

# 使用xpaht 第二种写法
# driver.find_element_by_xpath("//*[text()='WLAN']").click()

# driver.find_element_by_xpath("//*[text()='WLAN']").click()
driver.find_element_by_xpath("//*[@text='WLAN']").click()

sleep(3)
driver.quit()








