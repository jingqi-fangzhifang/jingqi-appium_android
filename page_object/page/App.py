#!_*_coding:utf-8_*_
#author:jingqi
from driver.Client import AndroidClient
from page.BasePage import BasePage
from page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return MainPage()