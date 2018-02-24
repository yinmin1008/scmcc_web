# -*- coding:utf-8 -*-
__author__ = 'snake'

'''
Created on 2017年3月7日
@author: snake
'''

import xml.etree.ElementTree as ET
from config import config


class XmlUtils:

    @staticmethod
    def read_xml_document(xml_path, case_name):
        case_words = []
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
        except Exception:
            raise Exception("解析数据XML时发生异常，请检查XML格式")

        # 遍历XML所有节点
        for child in root:
            for son in child:
                if case_name in son.attrib.values():
                    case_words.append(son.attrib)

        return case_words


"""解析XML，实现PO层"""
if __name__ == "__main__":
    print(XmlUtils.read_xml_document(config.DATA_FILE_PATH, "test_search_fail"))
