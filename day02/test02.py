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

el1 = driver.find_element_by_xpath('//*[contains(@text, "存储")]')

el2 = driver.find_element_by_xpath('//*[contains(@text, "WLAN")]')

driver.scroll(el1, el2)
sleep(3)
driver.quit()
