# -*- coding:utf-8 -*-
__author__ = 'snake'

import datetime, sys


TEST_WAP_URL = "http://wap.sc.10086.cn/wap/login.html"
TEST_WEB_URL = "http://www.sc.10086.cn/service/my/SC_MY_INDEX.html"
TEST_ROOT_URL = "http://www.baidu.com/"


""" 项目package变量路径
"""
PRO_ROOT_PATH = "C:\\Users\\SNake\\PycharmProjects\\scmcc_web"  # 项目root目录
PRO_CONFIG_PATH = PRO_ROOT_PATH + "\\config\\"  # 项目config目录
PRO_DATA_PATH = PRO_ROOT_PATH + "\\data\\"  # 项目data目录
PRO_DRIDERS_PATH = PRO_ROOT_PATH + "\\drivers\\"  # 项目drivers目录
PRO_LOG_PATH = PRO_ROOT_PATH + "\\log\\"  # 项目log目录
PRO_REPORT_PATH = PRO_ROOT_PATH + "\\report\\"  # 项目report目录
PRO_SRC_PATH = PRO_ROOT_PATH + "\\src\\"  # 项目src目录
PRO_SRC_TEST_PATH = PRO_ROOT_PATH + "\\src\\test\\"  # 项目src/test目录
PRO_SCR_TEST_CASE_PATH = PRO_ROOT_PATH + "\\src\\test\\case\\"  # 项目src/test/case目录
PRO_SCR_TEST_COMMON_PATH = PRO_ROOT_PATH + "\\src\\test\\common\\"  # 项目src/test/common目录
PRO_SCR_TEST_PAGE_PATH = PRO_ROOT_PATH + "\\src\\test\\page\\"  # 项目src/test/page目录
PRO_SCR_TEST_SUITE_PATH = PRO_ROOT_PATH + "\\src\\test\\suite\\"  # 项目src/test/suite目录
PRO_SRC_UTILS_PATH = PRO_ROOT_PATH + "\\src\\utils\\"  # 项目src/utils目录
RPO_SRC_TEST_SROUCES = PRO_ROOT_PATH + "\\src\\test\\sources\\"

""" 测试数据文件目录
"""
DATA_FILE_PATH = PRO_DATA_PATH + "testdata.xml"

""" 测试日志文件名
"""
LOG_FILE_NAME = PRO_LOG_PATH + datetime.datetime.now().strftime("%Y-%m-%d.log")

""" 测试报告文件名
"""
date = datetime.datetime.now()
REPORT_SUCCESS_FILE_NAME = PRO_REPORT_PATH + datetime.datetime.now().strftime(
    "%Y-%m-%d\\") + "TEST_REPORT_" + date.strftime("%Y_%m_%d %H_%M_%d.html")
