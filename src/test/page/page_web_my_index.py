# -*- coding:utf-8 -*-
__author__ = 'snake'



class WebMyIndex():
    def __init__(self, **kwargs):
        self.driver = kwargs.get("driver")
        self.page_title = self.driver.find_element_by_id("wdyd_nav_a") # iframe标题

        self.user_phone = self.driver.find_element_by_id("userPhone") # 用户手机号
        self.user_city = self.driver.find_element_by_id("userCity") # 号码归属地

        self.curren_score = self.driver.find_element_by_id("score") # 当前余额
        self.current_bal = self.driver.find_element_by_id("currentBal") # 当前余额
        self.current_remain = self.driver.find_element_by_id("currentRemain") # 剩余流量






