# -*- coding:utf-8 -*-
__author__ = 'snake'


from config import config
from selenium import webdriver


def get_demo_driver():
    driver = webdriver.Chrome(config.PRO_DRIDERS_PATH + 'chromedriver-2.35.exe')
    driver.get(config.TEST_ROOT_URL)
    driver.maximize_window()

    return driver


def get_web_driver():
    driver = webdriver.Chrome(executable_path=config.PRO_DRIDERS_PATH + 'chromedriver-2.35.exe')
    driver.get(config.TEST_WEB_URL)
    driver.maximize_window()

    return driver


def get_wap_driver():
    driver = webdriver.Chrome(executable_path=config.PRO_DRIDERS_PATH + 'chromedriver-2.35.exe')
    driver.get(config.TEST_WAP_URL)
    driver.maximize_window()

    return driver


def is_element_exist(driver, element):
    try:
        driver.find_element(element)
        return True
    except :
        return False
