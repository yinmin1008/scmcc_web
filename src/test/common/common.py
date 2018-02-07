# -*- coding:utf-8 -*-
__author__ = 'snake'



from config import config



def get_browser():
    from selenium import webdriver
    browser = webdriver.Chrome(config.PRO_DRIDERS_PATH + 'chromedriver-2.34.exe')
    browser.get(config.TEST_ROOT_URL)

    return browser