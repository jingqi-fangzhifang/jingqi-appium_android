#!_*_coding:utf-8_*_
# author:jingqi

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiuAndroidLogin(object):
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
        self.driver = self.restart_appium()
        el1 = self.driver.find_element_by_id("com.sankuai.meituan:id/permission_agree_btn")
        el1.click()
        el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el2.click()
        self.driver.implicitly_wait(5)
        el3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        el3.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.sankuai.meituan:id/city_search_edit_btn").send_keys("杭州")
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayou")
        el5.click()

    def test_login_error_username(self):
        self.driver.implicitly_wait(5)
        el6 = self.driver.find_element_by_xpath('//*[@text="马上登录"]')
        el6.click()

        el7 = self.driver.find_element_by_id('passport_mobile_phone').send_keys("")





    def test_login_error_password(self):
        pass

    def teardown_method(self):
        print("退出美团")
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(["-s", "test_appium.py"])
