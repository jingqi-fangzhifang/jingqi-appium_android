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
        # cls.driver = cls.init_Appium()

    def setup_method(self):
        print("setup method")
        pass

    def test_webview_simulator_A(self):
        # 测试webview
        self.driver.find_element_by_accessibility_id("A股开户").click()
        pass

    def teardown_method(self):
        print("后退")
        self.driver.back()


if __name__ == "__main__":
    pytest.main(["-s", "test_appium.py"])
