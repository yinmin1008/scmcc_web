# -*- coding:utf-8 -*-
__author__ = 'snake'



from config import config



def get_browser():
    from selenium import webdriver
    browser = webdriver.Chrome(config.PRO_DRIDERS_PATH + 'chromedriver-2.34.exe')
    browser.get(config.TEST_ROOT_URL)

    return browser

def get_web_driver():
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path=config.PRO_DRIDERS_PATH + 'chromedriver-2.34.exe')
    driver.get(config.TEST_WEB_URL)
    driver.add_cookie(
        {'name': 'JSESSIONID', 'value': 'jAPQF-krR_ADqMuLicmZuUxWL9dJaYMjS8Ynn0KW0sbNLPBw3yn9!-915567757'})
    driver.add_cookie({'name': 'SC_WTCX_SC_MY_ZDCX', 'value': 'SC_MY_ZDCX+1519464524069'})
    driver.add_cookie({'name': 'city', 'value': 'CDDQ'})
    driver.add_cookie({'name': 'topUserMobile', 'value': ''})
    driver.add_cookie({'name': 'xwt', 'value': 'r_xwt_108'})
    driver.get("http://www.sc.10086.cn/service/login.html?url=my/SC_MY_INDEX.html")

    return driver



def get_wap_driver():
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path=config.PRO_DRIDERS_PATH + 'chromedriver-2.34.exe')
    driver.get(config.TEST_WAP_URL)
    driver.add_cookie(
        {'name': 'JSESSIONID', 'value': 'Zg7mH7wh0QbRAQhdc2WkK_jkBs3APL2UvBMXBAYuIsqmiOR6cxiO!-904159996'})
    driver.add_cookie(
        {'name': 'scwap_uli', 'value': 'ep_U5sgT9-Zrs33js_pn_CCyW1Wxv0Y7w-hzS0mVc9GOtODmPw95!1908483680!1519695349779'})
    driver.add_cookie({'name': 'scwap_uli_ic', 'value': 'dcc0eb9a90d746fb90d5cfc90e1c98c8'})
    driver.add_cookie({'name': 'scwap_uli_rem', 'value': '206428f00eca48579d3d93dccb269c20'})
    driver.add_cookie({'name': 'scwap_ulo', 'value': '0'})
    driver.add_cookie({'name': 'WT_FPC', 'value': 'id=23bee684bcca92482ee1519463807137:lv=1519984294685:ss=1519984294685'})
    driver.get(config.TEST_WAP_URL)

    return driver



def is_element_exist(driver, element):
    try:
        driver.find_element(element)
        return True
    except :
        return False
