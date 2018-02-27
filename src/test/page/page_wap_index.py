# -*- coding:utf-8 -*-
__author__ = 'snake'



class MyIndexPage():
    def __init__(self, **kwargs):
        self.driver = kwargs.get("driver")
        self.user_phone = self.driver.find_element_by_class_name("user-number")
        self.flow_used = self.driver.find_element_by_xpath("//*[@id='js-personal-flow']/ul/li[1]/strong")
        self.flow_surplus = self.driver.find_element_by_xpath("//*[@id='js-personal-flow']/ul/li[2]/strong")
        self.flow_internal_surplus = self.driver.find_element_by_xpath("//*[@id='js-personal-flow-G0']/div/div/div[1]/strong")
        self.flow_provice_surplus = self.driver.find_element_by_xpath("//*[@id='js-personal-flow-G1']/div/div/div[1]/strong")
        self.flow_intel_free_surplus = self.driver.find_element_by_xpath("//*[@id='js-personal-flow-G2']/div/div/div[1]/strong")
        self.flow_prov_free_surplus = self.driver.find_element_by_xpath("//*[@id='js-personal-flow-G3']/div/div/div[1]/strong")
        self.flow_anxin_time = self.driver.find_element_by_xpath("//*[@id='js_ax_flow']/ul/li/span")





