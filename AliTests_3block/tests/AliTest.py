#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from unittest import TestCase
import unittest
from selenium import webdriver
from Pages.pages import Pages
import time
class AliTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.pages = Pages(cls.driver)
        cls.pages.open("http://ru.aliexpress.com/")

    #test_minmax
    def test_1(self):
        min=4000
        max=8000
        self.pages.page_main.search_bar_template.search(u'ноутбук')
        self.pages.page_search_result.search_criteria.criteria_price(min,max)
        self.pages.page_search_result.filter_sort.sort_result_by_price()
        self.assertTrue(float(self.pages.page_search_result.result_list_goods.get_price(1)) >= float(min), u"Найден товар не входящий в границы поиска(min)")
        self.pages.page_search_result.filter_sort.sort_result_by_price()
        self.assertTrue(float(self.pages.page_search_result.result_list_goods.get_price(1)) <= float(max), u"Найден товар не входящий в границы поиска(max)")

    #test_total_price
    def test_2(self):
        self.pages.page_main.search_bar_template.search(u'пылесос')
        self.pages.page_search_result.search_criteria.free_ship_click()
        temp_total_price = 0
        for i in range(1,4):
            self.pages.page_search_result.result_list_goods.open_product(i)
            temp_total_price+=self.pages.page_goods.goods_info.get_price()
            self.pages.page_goods.goods_info.button_add_to_cart_click()
            self.pages.page_goods.goods_info.choice_go_to_page_goods()
            self.pages.back()
        self.pages.search_bar_template.go_to_shop_cart()
        self.assertTrue(temp_total_price == self.pages.page_cart.added_goods.get_total_price(), u'Не верная цена')

    #test_remove_from_cart
    def test_3(self):
        self.pages.search_bar_template.go_to_shop_cart()
        count=self.pages.page_cart.added_goods.count
        while count != 0:
            self.pages.page_cart.added_goods.remove_goods(1)
            count-=1
        self.assertEqual(0, self.pages.page_cart.added_goods.count, u'В корзине неверное количество наименований')

    #test_add_to_cart
    def test_4(self):
        self.pages.page_main.search_bar_template.search(u'ноутбук')
        for i in range(1,4):
            self.pages.page_search_result.result_list_goods.open_product(i)
            self.pages.page_goods.goods_info.button_add_to_cart_click()
            self.pages.page_goods.goods_info.choice_go_to_page_goods()
            self.pages.back()
        self.pages.search_bar_template.go_to_shop_cart()
        self.assertEqual(3, self.pages.page_cart.added_goods.count, u'В корзине неверное количество наименований')

    #test_quantity
    def test_5(self):
        self.pages.page_main.search_bar_template.search(u'пила')
        self.pages.page_search_result.result_list_goods.open_product(1)
        self.pages.page_goods.goods_info.set_quantity(9)
        self.pages.page_goods.goods_info.button_add_to_cart_click()
        self.pages.page_goods.goods_info.choice_go_to_page_cart()
        quantity=self.pages.page_cart.added_goods.get_quantity_item(1) #последний добавленный
        self.assertEqual(9,quantity, u'Не верное количество добавленного товара')





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
