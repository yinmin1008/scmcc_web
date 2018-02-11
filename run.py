# -*- coding:utf-8 -*-
__author__ = 'snake'

import xmlrunner,re,unittest
from config import config
from src.test.case import *
from unittest import TextTestRunner
from src.test.suite.testsuites import TestSuites


def get_result_method(testresult):
    results = []
    for id, error_reason in testresult:
        result = {}
        test_method = re.findall("(.+?)_\d", id._testMethodName)
        if len(test_method) == 0:
            result["method"] = id._testMethodName
        else:
            result["method"] = test_method[0]

        result["class"] = id.__class__.__name__
        result["module"] = id.__class__.__module__
        results.append(result)

    return results



if __name__ == "__main__":
    test_suites = TestSuites().get_testsuites()
    #runner = xmlrunner.XMLTestRunner(output=config.PRO_REPORT_PATH)
    runner = TextTestRunner(verbosity=1)
    result = runner.run(test_suites)

    # 收集失败/错误的case
    error_cases = get_result_method(result.errors)
    fail_cases = get_result_method(result.failures)


    # 跑error用例
    if config.RETEST_ERROR_CASES:
        for case in error_cases:
            test_suites = unittest.TestSuite(unittest.makeSuite(case.get("module").case.get("class")))#加载时出现问题
        runner = TextTestRunner(verbosity=1)
        result = runner.run(test_suites)

    # 跑失败用例
    if config.RETEST_FAILED_CASES:
        print(fail_cases)




