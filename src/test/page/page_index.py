# -*- coding:utf-8 -*-
__author__ = 'snake'

from src.test.page.page_search_result import SearchResultPage
from selenium import webdriver


class IndexPage():
    def __init__(self, **kwargs):
        self.browser = kwargs.get("browser")
        self.ky = self.browser.find_element_by_id("kw")
        self.su = self.browser.find_element_by_id("su")
        self.news = self.browser.find_element_by_name("tj_trnews")


    def search(self):
        self.ky.send_keys("123")
        self.su.click()

        # 返回操作后的页面对象，用于后期处理
        return SearchResultPage(self.browser)

    def news_link(self):
        self.news.click()
