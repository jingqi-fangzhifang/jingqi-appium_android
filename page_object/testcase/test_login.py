#!_*_coding:utf-8_*_
#author:jingqi
import pytest

from page.App import App


class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.ProFilePage = cls.ProFilePage = App.main().gotoProFile()

    def setup_method(self):
        self.LoginPage = self.ProFilePage.gotoLogin()

    @pytest.mark.parametrize("user,pw,msg",[
        ("15265841255", "123456","手机号码"),
        ("15265841256", "123456", "手机号码"),
        ("15265841257", "123456", "密码")])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        # todo: 点击x号 返回到之前页面
        self.loginPage.back()

