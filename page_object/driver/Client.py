#!_*_coding:utf-8_*_
# author:jingqi
from appium import webdriver
from time import sleep
import yaml
class AndroidClient:
    driver: webdriver.Remote
    platform = "android"
    @classmethod
    def install_app(cls: webdriver.Remote):
        #print("美进行初始化")
        #caps = {}
        #caps["platformName"] = "android"
        #caps["deviceName"] = "demo"
        #caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        #caps["appPackage"] = "com.xueqiu.android"
        #caps["autoGrantpermissions"] = True  # 管理员
        #caps['resetKeyBoard'] = True
        #cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #cls.driver.implicitly_wait(10)
        #sleep(5)
        #return cls.driver

        return cls.initDriver("restart_app")

    @classmethod
    def restart_app(cls):
        #print("重新启动雪球")
        #caps = {}
        #caps["platformName"] = "Android"
        #caps["deviceName"] = "demo"
        #caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        #caps["appPackage"] = "com.xueqiu.android"
        #caps["noRest"] = True  # 不重置
        #caps['resetKeyBoard'] = True,
        #caps['unicodekeyboard'] = True
        #cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #cls.driver.implicitly_wait(10)
        #sleep(5)
        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls, key):
        driver_data = yaml.load(open("../data/driver.yaml",))
        caps: dict = driver_data[key]["caps"]
        server: str = driver_data[key]["server"]
        implicitly_wait = int(driver_data[key]["implicitly_wait"])
        platform = str(driver_data["platform"])
        cls.platform = platform
        #if platform.lower() == "android":
        #    caps = driver_data[key]['caps']["android"]
        # 支持多平台
        caps = driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)


if __name__ == "__main__":
    main = AndroidClient()
    main.driver.find_element_by_id()
