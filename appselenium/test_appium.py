#!_*_coding:utf-8_*_
# author:jingqi

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiuAndroid(object):
    driver: webdriver.Remote = None

    @classmethod
    def init_Appium(cls: webdriver.Remote):
        print("美团进行初始化")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.01:62001"
        caps["appActivity"] = "com.meituan.android.pt.homepage.activity.MainActivity"
        caps["appPackage"] = "com.sankuai.meituan"
        caps["autoGrantpermissions"] = "true"  # 管理员
        caps['resetKeyBoard'] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver

    @classmethod
    def restart_appium(cls):
        print("重新启动美团")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.01:62001"
        caps["appActivity"] = "com.meituan.android.pt.homepage.activity.MainActivity"
        caps["appPackage"] = "com.sankuai.meituan"
        caps["noRest"] = True  # 不重置
        caps['resetKeyBoard'] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        return driver

    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.driver = cls.init_Appium()

    def setup_method(self):
        print("setup method")
        TestXueqiuAndroid.driver = self.restart_appium()

    def test_login(self):
        print("定位等信息_test_login")
        el1 = self.driver.find_element_by_id("com.sankuai.meituan:id/permission_agree_btn")
        el1.click()
        el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el2.click()
        self.driver.implicitly_wait(5)
        el3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el3.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sankuai.meituan:id/city_search_edit_btn").send_keys("杭州")
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayou")
        el5.click()
        assert True

    def test_waimai(self):
        print("搜素外卖_test_waimai")
        self.driver.find_element_by_id("")

    def test_swipe(self):
        # 到首页进行滑动
        TestXueqiuAndroid.driver.swipe()

    def test_action(self):
        # 测试滑动操作
        action = TouchAction(self.driver)
        action.press(x=1000, y=1000).move_to(x=200, y=200).release().perform()

    def test_action_p(self):
        # 测试滑动操作,使用百分比
        print(self.driver.get_window_rect())
        rect = self.driver.get_window_rect()
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=rect["width"] * 0.8, y=rect["height"] * 0.8).move_to(x=rect["width"] * 0.2, y=rect["height"] * 0.2).release().perform()


    def teardown_method(self):
        print("退出美团")
        TestXueqiuAndroid.driver.quit()


if __name__ == "__main__":
    pytest.main(["-s", "test_appium.py"])
