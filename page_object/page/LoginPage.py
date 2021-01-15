#!_*_coding:utf-8_*_
# author:jingqi
from selenium.webdriver.support.wait import WebDriverWait

from page.BasePage import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_close")
    _other_locator = (By.ID, "tv_login_by_phone_or_others")
    _register_phone_number = (By.ID, "register_phone_number")
    _register_code = (By.ID, "register_code")
    _button_next = (By.ID, "button_next")
    _tv_login_with_account = (By.ID, "tv_login_with_account")
    _login_account = (By.ID, "login_account")
    _login_password = (By.ID, "login_password")
    _close2_locator = (By.ID, "iv_action_back")
    _error_msg = (By.ID, "md_content")
    _back_locator = (By.XPATH, '//*[contains(@resource-id,"iv_close") or contains(@resource-id,"iv_action_back"]')

    def loginByWX(self):
        return self

    def loginByMSG(self, phone, code):
        return self

    # 重新实现
    def loginByPassword(self, account, password):
        # todo: load from yaml
        # self.loadSteps("../data/LoginPage.yaml")
        self.loadSteps("../data/LoginPage.yaml", "loginByPassword", var1=account, var2=password)

    """
    def loginByPassword(self, account, password):
        # 登录失败
        self.find(self._other_locator).click()
        self.find(self._tv_login_with_account).click()
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()
        return self
    """

    def loginSuccessByPassword(self, account, password):
        # 登录成功
        from page.MainPage import MainPage
        return MainPage()

    def getErrorMsg(self) -> str:
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg

    def back(self):
        # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self._close_locator))
        self.find(self._back_locator).click()
        from page.ProFilePage import ProFilePage
        return ProFilePage()
