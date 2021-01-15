#!_*_coding:utf-8_*_
# author:jingqi
from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self

    def getPriceByName(self, name: str) -> float:
        # todo:获取其中一个数据，返回出来
        price = self.driver.find_element_by_xpath('//*[@text="{}"]'.format(name)).text

        priceLocator = (By.XPATH, '//*[@text="{}"]'.format(name))
        price = self.find(priceLocator).text

        return float(price)
