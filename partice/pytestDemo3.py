#!_*_coding:utf-8_*_
# author:jingqi
import pytest


# autouse  自动应用
@pytest.fixture()
def open_browser():
    print("打开浏览器，打开百度首页")

    yield
    print("执行tearDown")
    print("关闭浏览器")


# 使用部分应用
@pytest.mark.usefixtures("open_browser")
def test_soso():
    print("登录后搜索")


def test_cancan():
    print("不需要登录")


@pytest.mark.usefixtures("open_browser")
def test_car():
    print("需要登录，加购物车")
