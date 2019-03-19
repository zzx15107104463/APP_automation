import time

from appium import webdriver

desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填
desired_caps['deviceName'] = '192.168.56.101:5555'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# if driver.is_app_installed("com.vcooline.aike"):
#     driver.remove_app("com.vcooline.aike")
#     print('卸载完成')
# else:
driver.install_app('c:\\BaiNianAoLai.apk')
print('安装成功')
time.sleep(3)
driver.quit()
