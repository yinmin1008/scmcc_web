# -*- coding:utf-8 -*-
__author__ = 'snake'

import xmlrunner
from config import config
from src.test.suite.testsuites import TestSuites
from unittest import TextTestRunner


"""
    1. 执行每一个测试用例
    2. 在执行时，每个case代码获取xml数据
    3. 若当前case存在数据，则根据数据条数执行循环；若不存在数据，则按照代码中的默认数据执行
    4. 数据精度为每一个方法：单功能=配但数据；业务流功能=配业务流数据。

"""


if __name__ == "__main__":
    test_suites = TestSuites().get_testsuites()
    #runner = xmlrunner.XMLTestRunner(output=config.PRO_REPORT_PATH)
    runner = TextTestRunner(verbosity=2)
    runner.run(test_suites)


