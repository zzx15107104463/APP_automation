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
# 解决中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search").click()

# 输入内容  send_keys()
el = driver.find_element_by_id("android:id/search_src_text")
# 输入英文
# el.send_keys("adc")
# 输入中文
el.send_keys("哈喽")
# 清空 已输入的内容
el.clear()

sleep(3)
driver.quit()
