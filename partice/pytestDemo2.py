#!_*_coding:utf-8_*_
#author:jingqi

import pytest


@pytest.fixture(scope="module")
def open_browser():
    print("打开浏览器，打开百度首页")

    yield
    print("执行tearDown")
    print("关闭浏览器")


def test_search(open_browser):
    print("查找")

