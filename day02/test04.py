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
battery = driver.find_element_by_xpath('//*[@text="电池"]')

wlan = driver.find_element_by_xpath('//*[@text="WLAN"]')

driver.drag_and_drop(battery, wlan)

driver.find_element_by_xpath('//*[@text="安全"]').click()

driver.find_element_by_xpath('//*[@text="屏幕锁定方式"]').click()

driver.find_element_by_xpath('//*[@text="图案"]').click()

sleep(2)
TouchAction(driver).press(x=240, y=850).wait(100).move_to(x=719 - 240, y=0).wait(100). \
    move_to(x=1200 - 719, y=0).wait(100).move_to(x=719 - 1200, y=1330 - 850).wait(100). \
    move_to(x=240 - 719, y=1806 - 1330).wait(100).move_to(x=719 - 240, y=0).wait(100). \
    move_to(x=1200 - 719, y=0).wait(100).release().perform()

sleep(3)
driver.quit()
