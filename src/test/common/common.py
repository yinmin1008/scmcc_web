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
        {'name': 'JSESSIONID', 'value': 'o9zHGbs2k53FVi_aFuJgU82k8a7sgzA6wY-_lap-VlwPbGUfxfMb!-915567757'})
    driver.add_cookie({'topUserMobile': 'scwap_uli_ic', 'value': ''})
    driver.add_cookie({'xwt': 'scwap_uli_rem', 'value': 'r_xwt_108'})
    driver.get(config.TEST_WEB_URL)

    return driver



def get_wap_driver():
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path=config.PRO_DRIDERS_PATH + 'chromedriver-2.34.exe')
    driver.get(config.TEST_WAP_URL)
    driver.add_cookie(
        {'name': 'JSESSIONID', 'value': '0KTG7GoyDm1AXNKiVWU43hwJpPtKdALsquQXhz2WQzjV1cVc2FWg!1908483680'})
    driver.add_cookie(
        {'name': 'scwap_uli', 'value': 'ZjvG7GKq6ToW2Joi1Wz1mmAfaAHPVFXbdbljjR0EoIu2xzCyAc_R!-904159996!1519460836010'})
    driver.add_cookie({'name': 'scwap_uli_ic', 'value': 'f152b1314e1f4c34b3039dbf342f64e8'})
    driver.add_cookie({'name': 'scwap_uli_rem', 'value': 'b28da43a21434b918119ca75fbc091fb'})
    driver.add_cookie({'name': 'scwap_ulo', 'value': '0'})
    driver.get(config.TEST_WAP_URL)

    return driver