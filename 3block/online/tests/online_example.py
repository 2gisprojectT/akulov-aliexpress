#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page

class SeleniumTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'кафе')
        self.assertTrue(page.search_result.count > 0, 'Wrong count of firms')
        driver.close()

    def test_share(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search(u'кафе')
        count = page.search_result.count
        page.open(page.extra_group.get_url_share())
        self.assertEqual(u'кафе', page.search_bar.get_str_search(), u'Не верна строка поиска')
        self.assertEqual(count, page.search_result.count, u'Не верно количество фирм')
        driver.close()

    def test_route(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search_route(u'Студенческая',u'Заельцовская')
        self.assertTrue(0 < page.search_result_route.count_steps_route, u'Не найден путь')
        driver.close()


if __name__ == '__main__':
    unittest.main()
