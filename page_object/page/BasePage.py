#!_*_coding:utf-8_*_
# author:jingqi
from selenium.webdriver.remote.webelement import WebElement

from driver.Client import AndroidClient
from selenium.webdriver.common.by import By
import yaml


class BasePage:
    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, *args) -> WebElement:
        # todo:处理各类弹窗
        return self.driver.find_element(args)

    def findByText(self, text: str) -> WebElement:
        return self.driver.find(By.XPATH, '//*[@text={}]'.format(text))

    def loadSteps(self, po_path, key, **kwargs):
        # todo 解析yaml
        file = open(po_path, 'r')
        po_data = yaml.load(file)
        po_method = po_data[key]
        if po_data.keys().__contains__("elements"):
            po_elements = po_data["elements"]
        for step in po_method:
            step: dict
            if step.keys().__contains__("element"):
                element_platform = po_elements[step["element"]][AndroidClient.platform]
            else:
                element_platform = {"by":step["by"], "value": step["locator"]}
            element = self.driver.find_element(by=element_platform['by'], value=element_platform['locator'])
            #element = self.driver.find_element(by=step['by'], value=step['locator'])
            action = str(step["action"]).lower()
            # todo:定位失败 多数是因为弹窗， try exception 进入一个弹窗处理 元素的智能等待
            if action == "click":
                element.click()
            elif action == "sendkeys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s"%k, v)
                    print("update text: {}".format(text))
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND {} ".format(step))



