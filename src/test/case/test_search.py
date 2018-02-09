# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from ddt import data,ddt,file_data,unpack
from config import config
from src.test.common import common
from src.utils.util_xml import XmlUtils
from src.test.page.page_index import IndexPage


@ddt
class TestCaseLogin(unittest.TestCase):

    # 测试方法执行前执行
    def setUp(self):
        global keys
        self.browser = common.get_browser()
        keys = XmlUtils.read_xml_document(config.DATA_FILE_PATH, "test_search_fail")


    # 测试方法执行后执行
    def tearDown(self):
        self.browser.close()


    @data(*keys)
    def test_search_success(self, key):
        self.browser = common.get_browser()
        result_page = IndexPage(browser = self.browser).search(key.get("ky"))
        assert result_page.toindex.text == "百度首页"
        self.browser.close()

    def test_click_news(self):
        IndexPage(browser = self.browser).news_link()



if __name__ == "__main__":
    unittest.main()

