# -*- coding:utf-8 -*-
__author__ = 'snake'

import requests

def fuck_captcha(file_path):
    """
    返回验证码
    :param file_path:
    :return: 0为错误，其他为正确
    """
    try:
        file = open(file_path, 'rb').read()
        if "/" in file_path:
            filename = file_path.split("/")[-1]
        if "\\" in file_path:
            filename = file_path.split("\\")[-1]
        files = {'file': (filename, file)}
        crack_server1 = "http://localhost:87/scmccWapCaptchaCrack"
        crack_server = 'http://captcha.testjie.top/scmccWapCaptchaCrack'
        r = requests.post(crack_server, files=files)

        if r.status_code == 200:
            return eval(r.text).get("data")

        return "-"
    except Exception as e:
        raise e
        return "--"