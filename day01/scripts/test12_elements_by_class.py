
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
        2.使用class定位元素第三个(下标为2的元素)
"""

# 获取class  android.widget.TextView 所有元素
els = driver.find_elements_by_class_name("android.widget.TextView")
# 指定点击 下标为2的元素
# 指定点击 下标为3的元素
# els[3].click()

# 使用遍历来实现需求
for el in els:
    print(el)
    # if el.text == "WLAN":
    #     el.click()
    #     break


sleep(3)
driver.quit()








