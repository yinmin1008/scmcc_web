# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from src.test.common import common
from src.test.page.page_index import IndexPage


class TestCaseLogin(unittest.TestCase):

    # 测试方法执行前执行
    def setUp(self):
        self.browser = common.get_browser()
        print("setup")


    # 测试方法执行后执行
    def tearDown(self):
        self.browser.close()
        print("tearDown")


    def test_search_success(self):
        result_page = IndexPage(browser = self.browser).search()
        assert result_page.toindex.text == "百度首页"

    def test_click_news(self):
        IndexPage(browser = self.browser).news_link()



if __name__ == "__main__":
    unittest.main()

