# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from src.test.common import common
from src.test.page.page1_wap_index import MyIndexPage


class TestCaseIndex(unittest.TestCase):
    def setUp(self):
        self.driver = common.get_wap_driver()

    def tearDown(self):
        pass

    def test_user_a_phone(self):
        assert MyIndexPage().user_phone.text == "15008420344"

    def test_user_b_flow_used(self):
        assert MyIndexPage(driver=self.driver).flow_used.text != ""

    def test_user_c_flow_surplus(self):
        assert MyIndexPage(driver=self.driver).flow_surplus.text != ""

    def test_user_d_flow_internal_surplus(self):
        assert MyIndexPage(driver=self.driver).flow_internal_surplus.text != ""

    def test_user_e_flow_provice_surplus(self):
        assert MyIndexPage(driver=self.driver).flow_provice_surplus.text != ""

    def test_user_f_flow_intel_free_surplus(self):
        assert MyIndexPage(driver=self.driver).flow_intel_free_surplus.text != ""

    def test_user_g_flow_prov_free_surplus(self):
        assert MyIndexPage(driver=self.driver).flow_prov_free_surplus.text != ""

    def test_user_h_flow_anxin_time(self):
        assert MyIndexPage(driver=self.driver).flow_anxin_time.text != ""

