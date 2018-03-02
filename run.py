# -*- coding:utf-8 -*-
__author__ = 'snake'

import datetime, os
from config import config
from src.test.suite.testsuites import TestSuites
from src.utils.util_htmltestrunner import HTMLTestRunner



# def get_result_method(testresult):
#     results = []
#     for id, error_reason in testresult:
#         result = {}
#         test_method = re.findall("(.+?)_\d", id._testMethodName)# 通过正则表达式判断case是单次运行还是多次运行
#         if len(test_method) == 0:
#             result["method"] = id._testMethodName
#         else:
#             result["method"] = test_method[0]
#
#         result["class"] = id.__class__.__name__
#         result["module"] = id.__class__.__module__
#         results.append(result)
#
#     return results


# def test_fail_case(cases):
#     report_desc = "made by snake"
#     report_file = config.REPORT_FAILED_FILE_NAME
#     report_folder = config.PRO_REPORT_PATH + datetime.datetime.now().strftime("%Y-%m-%d\\")
#     report_title = "四川移动网厅" + datetime.datetime.now().strftime("%Y-%m-%d")+"错误case复测报告"
#
#     # 循环获取并运行失败的测试用例，将测试报告保存在对应的文件下，以天为单位
#     test_suites = unittest.TestSuite()
#     for key in cases:           # 循环error 和 fail
#         for case in cases[key]: # 循环error和fail里面的list
#             cls = case.get("class")
#             method = case.get("method")
#             module = case.get("module")
#             exec("from src.test.case." + module + " import " + cls)
#             ########问题出在这儿！！ 无法加载test，春节回来解决这个问题！！！
#
#             test_suites.addTest(eval(cls)(unittest.TestLoader().loadTestsFromTestCase(cls+"."+method)))
#
#     return run_test(report_desc, report_file, report_folder, report_title, test_suites)


def run_test(report_desc, report_file, report_folder, report_title, test_suites):
    if not os.path.exists(report_folder):
        os.mkdir(report_folder)

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc, retry=0)
        result = runner.run(test_suites)

    return result


if __name__ == "__main__":
    report_file = config.REPORT_SUCCESS_FILE_NAME
    report_folder = config.PRO_REPORT_PATH + datetime.datetime.now().strftime("%Y-%m-%d\\")
    report_title = "四川移动WAP厅 " + datetime.datetime.now().strftime("%Y-%m-%d") + " 自动测试报告"
    report_desc = datetime.datetime.now().strftime("%Y-%m-%d") + " WAP厅自动化测试报告，巡检结果仅供参考"

    # 第一次：跑所有case
    test_suites = TestSuites().get_testsuites()
    result = run_test(report_desc, report_file, report_folder, report_title, test_suites)

    # 解析结果并根据配置文件重跑指定case
    # retest_cases = {}
    # if config.RETEST_ERROR_CASES:
    #     retest_cases['error'] = get_result_method(result.errors)
    # if config.RETEST_FAILED_CASES:
    #     retest_cases['fail'] = get_result_method(result.failures)
    #
    # if len(retest_cases) != 0:
    #     test_fail_case(retest_cases)
    # #
    # # 第二次：跑error和失败的测试用例
    # if config.RETEST_ERROR_CASES:
    #     retesting_case(get_result_method(result.errors))
    #
    # if config.RETEST_FAILED_CASES:
    #     retesting_case(get_result_method(result.failures))
