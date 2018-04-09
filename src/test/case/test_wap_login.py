# -*- coding:utf-8 -*-
__author__ = 'snake'


import unittest,time
from src.test.common import common
from src.test.page.page_wap_login import LoginPage
from selenium.webdriver.support import expected_conditions as EC

# 数据驱动依赖
from config import config
from src.utils.util_xml import XmlUtils
from ddt import data,ddt,file_data,unpack


@ddt
class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        self.driver = common.get_wap_driver()


    def tearDown(self):
        pass


    # 登陆成功用例
    @data(*XmlUtils.read_xml_document(config.DATA_FILE_PATH, "test_login_success"))
    def test_login_success(self, key):
        login_page = LoginPage(driver=self.driver)
        username = key.get("username")
        password = key.get("password")
        index_page = login_page.service_login(username,  password)
        time.sleep(5)
        url = EC.url_contains("login.html")
        assert url(self.driver) == False


    # 登陆失败用例
    @data(*XmlUtils.read_xml_document(config.DATA_FILE_PATH, "test_login_failed"))
    def test_login_failed(self, key):
        login_page = LoginPage(driver=self.driver)
        index_page = login_page.service_login(key.get("username"), key.get("password"))
        time.sleep(5)
        url = EC.url_contains("login.html")
        assert url(self.driver)