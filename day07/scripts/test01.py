import os
import sys

import allure

sys.path.append(os.getcwd())



class Test01:
    @allure.step("新增地址方法被执行")
    def test001(self):
        allure.attach("点击新增地址按钮", "")
        allure.attach("点击新增输入收件人：","")
        allure.attach("点击新增输入手机号：","")
        allure.attach("点击新增输入收货地址：","")
        allure.attach("点击新增输入点击新增：","")
        print("test001被执行")

    # allure.attach("点击新增输入点击更新：", "")
    # @allure.step("更新地址方法被执行")
    def test002(self):
        print("test002被执行")