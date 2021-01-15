#!_*_coding:utf-8_*_
# author:jingqi
from selenium.webdriver.remote.webelement import WebElement

from driver.Client import AndroidClient
from selenium.webdriver.common.by import By
import yaml
import re

class BasePage:
    # 黑名单
    element_black = [(By.XPATH, "ddd")]
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
        return self.find(args)

    def find(self, by, value):
        # 重试3次  增加健壮性
        for i in range(3):
            try:
                element = self.driver.find_element(by, value)
            except Exception as e:
                pass
            finally:
                # 处理弹框
                # 找到页面的最顶级元素进行点击
                #get_max_element.click()  递归算法求最顶层数据
                pass
                ## 黑名单
                #self.driver.page_source
                #for e in BasePage.element_black:
                #    if re.match("sss", self.driver.page_source):
                #       elements =  self.driver.find_element(*e)
                #       if elements.__sizeof__() > 0:
                #          elements[0].click()




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



