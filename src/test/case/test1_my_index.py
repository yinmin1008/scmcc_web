# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from src.test.common import common
from src.test.page.page_web_my_index import WebMyIndex

class TestMyIndex(unittest.TestCase):
    def setUp(self):
        self.driver = common.get_web_driver()

    def tearDown(self):
        pass


    def test_user_phone(self):
        assert WebMyIndex(driver=self.driver).user_phone.text == "18408223928"
