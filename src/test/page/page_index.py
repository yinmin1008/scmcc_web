# -*- coding:utf-8 -*-
__author__ = 'snake'

from src.test.page.page_search_result import SearchResultPage


class IndexPage():
    def __init__(self, **kwargs):
        self.driver = kwargs.get("driver")
        self.ky = self.driver.find_element_by_id("kw")
        self.su = self.driver.find_element_by_id("su")
        self.news = self.driver.find_element_by_name("tj_trnews")


    def search(self, keyword):
        self.ky.send_keys(keyword)
        self.su.click()

        # 返回操作后的页面对象，用于后期处理
        return SearchResultPage(self.driver)

    def news_link(self):
        self.news.click()

