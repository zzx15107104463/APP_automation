# 导包
from appium import webdriver

desired_caps = {}

# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填
desired_caps['deviceName'] = '192.168.46.101:5555'

# APP包名
# desired_caps['appPackage'] = 'com.android.settings'
# 启动名
# desired_caps['appActivity'] = '.Settings'

# 不重置应用 数据保留
desired_caps['noReset'] = True

# 安装apk文件
desired_caps['app'] = "C:\\AK_CRM.apk"

# 指定连接设备
# desired_caps['udid'] = 'emulator-5554'
# desired_caps['udid'] = '192.168.86.101:5555'

# 获取driver
webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)