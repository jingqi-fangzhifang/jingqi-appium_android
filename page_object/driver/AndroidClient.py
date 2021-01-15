#!_*_coding:utf-8_*_
# author:jingqi
from appium import webdriver
from time import sleep

class AndroidClient:
    driver: webdriver.Remote

    @classmethod
    def init_app(cls: webdriver.Remote):
        print("美团进行初始化")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        caps["appPackage"] = "com.xueqiu.android"
        caps["autoGrantpermissions"] = True  # 管理员
        caps['resetKeyBoard'] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        sleep(5)
        return cls.driver

    @classmethod
    def restart_app(cls):
        print("重新启动雪球")
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        caps["appPackage"] = "com.xueqiu.android"
        caps["noRest"] = True  # 不重置
        caps['resetKeyBoard'] = True,
        caps['unicodekeyboard'] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        sleep(5)
        return cls.driver


if __name__ == "__main__":
    main = AndroidClient()
    main.driver.find_element_by_id()
