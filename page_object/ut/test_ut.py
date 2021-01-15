#!_*_coding:utf-8_*_
# author:jingqi

import yaml


class TestYaml():
    def test_yaml(self):
        dict = yaml.load(open("..\data\LoginPage.yaml", "r"))
        print(dict)
        for step in dict["loginByPassword"]:
            step: dict
            if step.keys().__contains__("element"):
                data = dict["elements"]
                print("此时的data--->",data)
            # print(step)
