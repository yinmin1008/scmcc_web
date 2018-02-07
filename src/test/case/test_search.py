# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from src.test.common import common
from src.test.page.index import Index


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
        Index(browser = self.browser).search()
        assert 1 == 1

    def test_click_news(self):
        Index(browser = self.browser).news_link()



if __name__ == "__main__":
    unittest.main()

