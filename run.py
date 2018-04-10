# -*- coding:utf-8 -*-
__author__ = 'snake'

import datetime, os
from config import config
from src.test.suite.testsuites import TestSuites
from src.utils.util_htmltestrunner import HTMLTestRunner
from src.utils.util_email import Mail



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


    # 运行calse所有case
    test_suites = TestSuites().get_testsuites()
    result = run_test(report_desc, report_file, report_folder, report_title, test_suites)

    # 邮件帐号密码、接受方密码
    MAIL_QQ_USER = "656882274@qq.com"
    MAIL_QQ_PWD = "qsumwxnxynttbbhj"
    MAIL_QQ_HOST = "smtp.qq.com"
    RECIPIENT = ["656882274@qq.com"]

    # 发送测试结果
    mail = Mail(MAIL_QQ_USER, MAIL_QQ_PWD, MAIL_QQ_HOST)
    mail.send_mail(RECIPIENT, report_title, report_desc, report_file)
