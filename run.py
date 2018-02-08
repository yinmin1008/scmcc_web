# -*- coding:utf-8 -*-
__author__ = 'snake'

import xmlrunner
from config import config
from src.test.suite.testsuites import TestSuites
from unittest import TextTestRunner


if __name__ == "__main__":
    test_suites = TestSuites().get_testsuites()
    #runner = xmlrunner.XMLTestRunner(output=config.PRO_REPORT_PATH)
    runner = TextTestRunner(verbosity=2)
    runner.run(test_suites)


