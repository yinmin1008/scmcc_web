# -*- coding:utf-8 -*-
__author__ = 'snake'

import os
from config import config
from src.test.page.page_base import BasePage
from src.test.page.demo_wap_index import MyIndexPage

class LoginPage(BasePage):
    def __init__(self, **kwargs):
        self.driver = kwargs.get("driver")
        self.img_close = self.find_element(type="id", value="closeImg")
        self.lab_service_pwd = self.find_element(value="/html/body/div[2]/form/div[1]/label[2]")
        self.input_user_mobile = self.find_element(value="//*[@id=\"js-user-mobile\"]")
        self.input_user_pwd = self.find_element(value="//*[@id=\"js-service-pwd\"]")
        self.input_verify_code = self.find_element(value="//*[@id=\"js-img-verifyCode\"]")
        self.img_code = self.find_element(value="//*[@id=\"js-img-code\"]")
        self.button_login = self.find_element(value="//*[@class='login-submit']/button")



    def _close_img(self):
        self.img_close.click()


    def _go_service_pwd_login(self):
        self.lab_service_pwd.click()


    def _get_img_code(self):
        temp = config.RPO_SRC_TEST_SROUCES + 'temp.png'
        file_name = config.RPO_SRC_TEST_SROUCES + "verifyCode.jpg"

        # 截图全屏图
        self.driver.save_screenshot(temp)

        left = self.img_code.location['x']
        top = self.img_code.location['y']
        right = self.img_code.location['x'] + self.img_code.size['width']
        bottom = self.img_code.location['y'] + self.img_code.size['height']

        # 需要配合Image库截图并发送识别...
        # im = Image.open(temp)
        # im = im.crop((left, top, right, bottom))
        # im.save(file_name)
        # captache = fuck_captache(file_name)
        captache = "0000"

        try:
            os.remove(temp)
            os.remove(file_name)
        except:
            pass
        finally:
            return captache


    def service_login(self, username, password):
        self._go_service_pwd_login()
        self._close_img()
        self.input_user_mobile.send_keys(username)
        self.input_user_pwd.send_keys(password)
        verify_code = self._get_img_code()
        self.input_verify_code.send_keys(verify_code)
        self.button_login.click()

        # 如果需要则返回下一页的对象供case使用
        #return MyIndexPage(driver=self.driver)



