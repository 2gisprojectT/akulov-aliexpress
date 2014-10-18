#-*-coding:utf8-*-
__author__ = 'Djonny'
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class TestMinMaxSD(TestCase):
    def test_minmax(self):
        min =4000
        max =8000
        driver = webdriver.Firefox()
        driver.get("http://ru.aliexpress.com/")
        driver.find_element_by_id("search-key").send_keys(u"ноутбук")
        WebDriverWait(driver.find_element_by_class_name("search-button").click(),30)

        driver.find_element_by_id("filter-price-from").send_keys(min)
        driver.find_element_by_id("filter-price-to").send_keys(max)
        WebDriverWait(driver.find_element_by_id("filter-price-to").send_keys(Keys.ENTER),30)


        WebDriverWait(driver.find_element_by_xpath("//div[@id='view-filter']/div[@class='narrow-down-bg'][5]/a").send_keys(Keys.ENTER),30)
        strmin = str(driver.find_elements_by_class_name("value")[0].text)
        strmin=strmin.replace(",",".").replace(" ","").replace(u"руб.","")
        print (float(strmin))
        self.assertFalse(float(min) <= float(strmin), u"Найден товар не входящий в границы поиска(min)")

        WebDriverWait(driver.find_element_by_xpath("//div[@id='view-filter']/div[@class='narrow-down-bg'][5]/a").send_keys(Keys.ENTER),30)
        strmax = str(driver.find_elements_by_class_name("value")[0].text)
        strmax=strmax.replace(",",".").replace(" ","").replace(u"руб.","")
        print (float(strmax))
        self.assertFalse(float(max) >= float(strmax), u"Найден товар не входящий в границы поиска(max)")
        driver.close()

class TestAddToBasket(TestCase):
    def test_Basket(self):

        driver = webdriver.Firefox()
        driver.get("http://ru.aliexpress.com/")
        driver.find_element_by_id("search-key").send_keys(u"ноутбук")
        WebDriverWait(driver.find_element_by_class_name("search-button").click(),30)

        lenmass=len(driver.find_elements_by_xpath("//ul[@id='hs-list-items']/li"))
        count=0

        while count!=lenmass:
            ssilka=driver.find_element_by_xpath("//ul[@id='hs-list-items']/li["+str(count+1)+"]/div[@class='detail']/h3/a")
            WebDriverWait(driver.get(ssilka.get_attribute('href')),30)
            WebDriverWait(driver.find_element_by_id("add-to-cart").send_keys(Keys.ENTER),30)
            driver.find_element_by_xpath("//div[@class='ui-window-btn']/button").click()
            WebDriverWait(driver.back(),30)
            count+=1

        WebDriverWait(driver.find_element_by_id("shop-cart").send_keys(Keys.ENTER),30)
        strcount=driver.find_element_by_xpath(".//span[@class='main-title-text-num']").get_attribute('innerHTML')
        count = strcount.replace(u" товар","").replace(u"а(ов)","")
        self.assertEqual(lenmass,int(count),u"В корзину добавлены не все указанные товары")

        massdel=driver.find_elements_by_link_text(u"Удалить")
        lenmassdel=len(massdel)
        count=0
        while count!=lenmassdel:
            WebDriverWait(driver.find_element_by_link_text(u"Удалить").send_keys(Keys.ENTER),30)
            count+=1

        try:
            driver.find_element_by_link_text(u"Удалить")
            result=True
        except:
            result=False
        self.assertEqual(False,result,u"Удаление из корзины работает не правильно")
        driver.close()


if __name__ == '__main__':
    unittest.main()