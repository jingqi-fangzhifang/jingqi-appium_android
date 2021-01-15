#!_*_coding:utf-8_*_
# author:jingqi

# 默认页面
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.ProFilePage import ProFilePage
from page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage
from time import sleep


class MainPage(BasePage):
    _profile_button = (By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")

    def gotoSelected(self):
        # todo:选择自选页，点击自选按钮
        self.driver.implicitly_wait(5)
        hangqing = (By.XPATH, '//*[contains(@resource-id,"tab_name") and @text="行情"]')
        self.driver.find(hangqing)
        self.find(hangqing).click()

        # self.driver.find_element_by_xpath('//*[contains(@resource-id,"tab_name") and @text="行情"]').click()

        print("开始休眠10秒钟")
        sleep(10)

        return SelectedPage()

    def gotoSearch(self):
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProFile(self):
        # self.find(MainPage._profile_button).click()
        self.loadSteps("../data/MainPage.yaml", "gotoProFile")
        return ProFilePage()
