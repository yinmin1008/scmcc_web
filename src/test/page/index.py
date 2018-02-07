# -*- coding:utf-8 -*-
__author__ = 'snake'

from selenium import webdriver

class Index():
    def __init__(self, **kwargs):
        self.browser = kwargs.get("browser")
        self.ky = self.browser.find_element_by_id("kw")
        self.su = self.browser.find_element_by_id("su")
        self.news = self.browser.find_element_by_name("tj_trnews")


    def search(self):
        self.ky.send_keys("123")
        self.su.click()

    def news_link(self):
        self.news.click()
