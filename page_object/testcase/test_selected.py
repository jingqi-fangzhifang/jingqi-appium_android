#!_*_coding:utf-8_*_
# author:jingqi
from page.App import App
import pytest

from page.MainPage import MainPage


class TestSelected:

    @classmethod
    def setup_class(cls):
        # 从首页开始
        cls.mainPage: MainPage = App.main()

    def setup_method(self):
        self.mainPage: MainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotoSearch()

    def test_price(self):
        # todo:
        assert self.mainPage.gotoSelected().getPriceByName("TCL科技") == 9.16

    def test_is_selected(self):
        srarchPage = self.searchPage.search("阿里巴巴")
        assert srarchPage.isInSelected("BABA") == False
        assert srarchPage.isInSelected("09988") == True

    @pytest.mark.parametrize("key, code", [
        ("招商银行", "SH600036"),
        ("平安银行", "SZ000001"),
        ("pingan",  "SH601318"),
    ])
    def test_is_selected_stock_hs(self, key, code):
        # todo:判断沪深股票在不在
        searchPage = self.searchPage.search(key)
        assert searchPage.isInSelected(code) == False

    def test_add_stock_hs(self):
        # TODO：添加沪深股票
        key = "招商银行"
        code = "SH600036"
        searchPage = self.searchPage.search(key)
        if searchPage.isInSelected(code) == True:
            # todo:已经在里面的话 先取消再添加
            searchPage.removeToSelected(code)

        searchPage.addToSelected(code)
        assert searchPage.isInSelected(code) == True

    def teardown_method(self):
        self.searchPage.cancel()

    def test_is_follow_user(self):
        # todo:
        pass


if __name__ == "__main__":
    pytest.main(["-s", "test_selected.py"])
