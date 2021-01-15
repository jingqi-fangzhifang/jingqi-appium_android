#!_*_coding:utf-8_*_
#author:jingqi


from page.BasePage import BasePage
from page.LoginPage import LoginPage


class ProFilePage(BasePage):
    def gotoLogin(self):
        # self.findByText("点击登录").click()
        self.loadSteps("../data/ProFilePage.yaml", "gotoLogin")
        return LoginPage()

