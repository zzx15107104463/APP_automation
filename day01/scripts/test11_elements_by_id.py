
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
        2.点击WLAN菜单栏(id定位对象列表中第1个)
"""
# 使用id定位一组元素
els = driver.find_elements_by_id("com.android.settings:id/title")


# els[0].click()
# print("获取的类型为：", type(els))
# print("长度为：", len(els))


# 遍历 获取所有元素
for el in els:
    if el.text == "WLAN":
        el.click()
        break
sleep(3)
driver.quit()








