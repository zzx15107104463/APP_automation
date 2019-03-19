from appium import webdriver
from time import sleep

# 前置代码、
# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
wlan = driver.find_element_by_xpath('//*[@text="WLAN"]')

wlan.click()

ssid = driver.find_element_by_xpath('//*[contains(@text, "SSID")]')
TouchAction(driver).long_press(ssid, duration=5000).perform()

sleep(3)
driver.quit()
