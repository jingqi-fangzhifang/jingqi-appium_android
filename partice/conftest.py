#!_*_coding:utf-8_*_
#author:jingqi

"""
共享文件
"""

import pytest


@pytest.fixture()
def login():
    print("登录")