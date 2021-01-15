#!_*_coding:utf-8_*_
# author:jingqi
import pytest

# autouse  自动应用
@pytest.fixture(scope="module", autouse=True)
def open_browser():
    print("打开浏览器，打开百度首页")

    yield
    print("执行tearDown")
    print("关闭浏览器")

def test_soso(login):
    print("登录后搜索")


def test_cancan():
    print("不需要登录")


def test_car(login):
    print("需要登录，加购物车")
