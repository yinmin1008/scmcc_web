# -*- coding:utf-8 -*-
__author__ = 'snake'


from config import config
from selenium import webdriver


class BasePage():

    # 封装find_element操作，默认为xpath
    def find_element(self, type="xpath", value=""):
        if type == "id":
            return self.driver.find_element_by_id(value)
        if type == "name":
            return self.driver.find_element_by_name(value)
        if type == "xpath":
            return self.driver.find_element_by_xpath(value)
        if type == "class":
            return self.driver.find_element_by_class_name(value)
