"""
    目标：app应用基础操作API
"""
# 导包
from appium import webdriver
from time import sleep

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

# 需求：判断爱客APK是否安装，如果安装进行卸载，如果没有安装进行安装操作

# 判断是否安装
if driver.is_app_installed("com.vcooline.aike"):
    # 卸载
    driver.remove_app("com.vcooline.aike")
    print("卸载完成！")
# 否则
else:
    # 安装
    driver.install_app("c:\\AK_CRM.apk")
    print("安装成功！")

# 暂停3秒
sleep(3)

# 关闭所有
driver.quit()

