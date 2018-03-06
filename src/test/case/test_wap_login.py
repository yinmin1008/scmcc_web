# -*- coding:utf-8 -*-
__author__ = 'snake'


import unittest
from src.test.common import common
from src.test.page.page_wap_login import LoginPage
from selenium.webdriver.support import expected_conditions as EC

class TestCaseLogin(unittest.TestCase):
    def setUp(self):
        self.driver = common.get_wap_driver()

    def tearDown(self):
        pass

    def test_login_success(self):
        login_page = LoginPage(driver=self.driver)
        index_page = login_page.service_login(username="15008520344", password="15008420344", verify_code="123456")
        url = EC.url_contains("login.html")
        assert url(self.driver) == False


    def test_login_failed(self):
        login_page = LoginPage(driver=self.driver)
        index_page = login_page.service_login(username="15008520344", password="15008420344", verify_code="123456")
        url = EC.url_contains("login.html")
        assert url(self.driver)