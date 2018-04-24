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

def send_mail(RECIPIENT, report_title, report_desc, report_file):
    # 初始化邮箱信息
    try:
        mail = Mail("656882274@qq.com", "qsumwxnxynttbbhj", "smtp.qq.com")
        mail.send_mail(RECIPIENT, report_title, report_desc, report_file)
    except Exception as e:
        print(e)


if __name__ == "__main__":

    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%d")
    report_file = config.REPORT_SUCCESS_FILE_NAME                                         # 测试报告文件
    report_folder = config.PRO_REPORT_PATH + \
                    datetime.datetime.now().strftime("%Y-%m-%d\\")                        # 测试报告文件夹
    report_title = "【异常反馈】+ 四川移动网厅自动化巡检 +" + now_date                    # 报告和邮件标题
    report_desc = now_date + " 四川移动网厅自动化测试巡检报告，测试结果可能仅供参考."     # 报告和邮件描述

    """运行所有case
    """
    test_suites = TestSuites().get_testsuites()
    result = run_test(report_desc, report_file, report_folder, report_title, test_suites)

    """errors反馈给测试
    """
    RECIPIENT = ["656882274@xwtec.cn"]    # 邮件接收
    errors = result.errors
    if errors:
        print("发现错误的case:", errors)
        print("发送错误的case的测试报告邮件...")

        # 邮件帐号密码/接受方密码
        report_title = "【错误反馈】 + 网厅 + " + now_date
        report_desc = "时间:%s\n" \
                      "类型:错误\n" \
                      "数量:%s\n" \
                      "堆栈信息： %s" \
                      % (now_date, str(len(errors)), errors)

        # 发送测试结果
        try:
            send_mail(report_title, report_desc, report_file)
        except Exception as e:
            print(e)

    """failures反馈给所有人
    """
    failures = result.failures
    if failures:
        print("发现异常case:", failures)
        print("发送异常case的测试报告邮件...")

        # 邮件帐号密码/接受方密码
        # RECIPIENT.append("656882274@qq.com")
        report_title = "【异常告警】 + 四川移动网厅自动化测试 +" + now_date
        report_desc = "时间:%s\n" \
                      "类型:错误\n" \
                      "数量:%s\n" \
                      "堆栈信息： %s" \
                      % (now_date, str(len(failures)), failures)

        # 发送测试结果
        try:
            send_mail(report_title, report_desc, report_file)
        except Exception as e:
            print(e)