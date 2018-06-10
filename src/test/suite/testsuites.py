# -*- coding:utf-8 -*-
__author__ = 'snake'

import unittest
from config import config


class TestSuites():
    def get_testsuites(self):
        test_suites = unittest.TestSuite()
        # 查找指定目录下、指定文件名开头的测试用例并组织测试套件
        all_cases = unittest.defaultTestLoader.discover(config.PRO_SCR_TEST_CASE_PATH, 'test_*.py')
        # 添加所有测试用例到测试套件
        test_suites.addTests(all_cases)

        return test_suites


if __name__ == "__main__":
    print(TestSuites().get_testsuites())



