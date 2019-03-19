
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
        2.使用xpath定位元素第四个(下标为3的元素)
"""

# 获取class  android.widget.TextView 所有元素
els = driver.find_elements_by_xpath("//*[contains(@class,'android.widget.TextView')]")

# 点击 下标为3的元素
els[3].click()


sleep(3)
driver.quit()








