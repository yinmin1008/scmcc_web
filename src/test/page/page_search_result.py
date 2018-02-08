# -*- coding:utf-8 -*-
__author__ = 'snake'


from selenium import webdriver

class SearchResultPage():
    def __init__(self, driver):
        self.driver = driver
        self.toindex = driver.find_element_by_class_name("toindex")

