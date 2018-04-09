# -*- coding:utf-8 -*-
__author__ = 'snake'

import requests


def fuck_captache(file_path):
    """
    返回验证码
    :param file_path:
    :return: 0为错误，其他为正确
    """
    try:
        files = {'file': open(file_path, 'rb').read()}
        r = requests.post('http://www.itblacklist.top/captachCrack/', files=files)
        return eval(r.text).get("data").get("Result")
    except:
        return 0000

if __name__ == "__main__":
    from config import config
    file_name = config.RPO_SRC_TEST_SROUCES + "verifyCode.jpg"
    print (fuck_captache(file_name))