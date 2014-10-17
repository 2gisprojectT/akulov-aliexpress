#-*-coding:utf8-*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SeleniumTest(TestCase):
    def test_search(self):
        driver = webdriver.Firefox()
        driver.get("http://2gis.ru/")
        elem = driver.find_element_by_class_name("suggest__input")
        elem.send_keys(u"khvvjv,v,v")
        search = driver.find_element_by_class_name("searchBar__submit")
        search.click()
        time.sleep(4)
        try:
            clicks = driver.find_element_by_class_name("mixedResults__geoTabNum")
            clicks.click()
            time.sleep(4)
            what = driver.find_element_by_class_name("mixedResults__geoTabNum")
            strwhat = what.text
            print(strwhat)
            assert 0 < strwhat
        except:
            nores=driver.find_element_by_class_name("noResults__title")
            strwhat=nores.text
            assert u"Увы, мы не знаем ответа на ваш вопрос" != strwhat
        driver.close()

if __name__ == '__main__':
    unittest.main()