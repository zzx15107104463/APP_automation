
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
    2.点击搜索按钮
    3.通过class定位方式点击输入框的返回按钮
"""

# 查找搜索按钮并点击
driver.find_element_by_id("com.android.settings:id/search").click()

# 使用class定位返回按钮
driver.find_element_by_class_name("android.widget.ImageButton").click()


sleep(3)
driver.quit()











sleep(3)

# 关闭所有
driver.quit()

