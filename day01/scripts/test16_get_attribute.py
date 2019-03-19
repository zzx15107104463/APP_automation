
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
  1.打开设置
  2.点击搜索按钮
  3.输入内容abc
  4.删除已输入abc
"""
# 点击搜索按钮
# el = driver.find_element_by_id("com.android.settings:id/search")

# 获取 搜索按钮的 name值  注意：name在android中不是元素的属性
# 使用name：返回 content-desc 或 text 文本值
# txt = el.get_attribute("name")
# print("使用name获取的值为：", txt)


# 使用 text 获取蓝牙元素文本
# result = driver.find_element_by_xpath("//*[contains(@text, '蓝牙')]").get_attribute("text")
# print("使用text获取的文本值为：", result)

# 使用 className 获取蓝牙 class属性值 注意：获取class属性时，使用的是className
# result = driver.find_element_by_xpath("//*[contains(@text, '蓝牙')]").get_attribute("className")
# print("使用class获取的文本值为：", result)


# 使用 resourceId 获取蓝牙 resource-id属性值 注意：获取resource-id属性时，使用的是resourceId
result = driver.find_element_by_xpath("//*[contains(@text, '蓝牙')]").get_attribute("resourceId")
print("使用resource-id获取的文本值为：", result)



sleep(3)
driver.quit()








