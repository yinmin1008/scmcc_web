# -*- coding:utf-8 -*-
__author__ = 'snake'


import logging
from config import config



log_level = logging.INFO
#log_level = logging.DEBUG
#log_level = logging.ERROR
#log_level = logging.WARNING


""" file_name:绝对路径
"""
def logger(file_name):
    format = '%(asctime)s %(levelname)-4s - %(funcName)s: %(message)s'
    logging.basicConfig(level=log_level, format=format, filename=file_name)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(format)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    return logging

def test1():
    logger(config.PRO_LOG_PATH + "123.log").info("222")


if __name__ == "__main__":
    test1()
