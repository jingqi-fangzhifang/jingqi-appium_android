#!_*_coding:utf-8_*_
# author:jingqi
from xmlrpc.client import Boolean

from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator = (By.ID, 'search_input_text')
    _click_locator = "BABA"

    def search(self, name):
        self.find(self._edit_locator).send_keys(name)
        self.findByText(self._click_locator).click()
        return self

    def addToSelected(self, key: str):
        follow_button = (By.XPATH, '//*[contains(@resource-id,"stockCode") and contains(@text, "{}")]/../../..//*['
                                   'contains( '
                                   '@resource-id,"add_attention")]'.format(key))
        self.driver.find(follow_button).click()
        # 表示返回的还是当前页
        return self

    def removeToSelected(self, key: str):
        followed_button = (By.XPATH, '//*[contains(@resource-id,"stockCode") and contains(@text, "{}")]/../../..//*['
                                     'contains( '
                                     '@resource-id,"add_attention")]'.format(key))
        self.driver.find(followed_button).click()
        # 表示返回的还是当前页
        return self

    def isInSelected(self, key) -> Boolean:
        # self.find(key)
        followed_button = (By.XPATH, '//*[contains(@resource-id,"stockCode") and contains(@text, "{}")]/../../..//*['
                                     'contains( '
                                     '@resource-id,"add_attention")]'.format(key))
        id = self.driver.find(followed_button).get_attribute("resourceId")
        return "followed_btn" in id

    def cancel(self):
        # 取消 回到首页
        self.findByText("取消").click()

    def searchByUser(self, key):
        # TODO：搜索用户
        pass

    def isFollowed(self):
        # todo :关注
        pass
