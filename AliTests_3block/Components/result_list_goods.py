#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from selenium.webdriver.common.keys import Keys

from Components.base_component import BaseComponent


class Result_list_goods(BaseComponent):

    selectors = {
        'self': '#hs-list-items',
        'first_item': '.list-item.list-item-first.util-clearfix.list-item-180',
        'item': '.list-item.util-clearfix.list-item-180',
    }

    selectors_item={
        'reference': '.detail > h3 > a',
        'price': '.info.infoprice .price.price-m .value',

    }



    @property
    def count(self):
        return len(self.driver.find_elements_by_css_selector(self.selectors['first_item']))+ \
               len(self.driver.find_elements_by_css_selector(self.selectors['item']))

    def __correct(self,number):
        if number < 1:
            raise
        if number==1:
           item=self.selectors['first_item']
        else:
            item=self.selectors['item']
        return item

    def open_product(self,number):
        try:
            item=self.__correct(number)
            if number != 1:
                item=item + ':nth-of-type('+str(number)+')'
        except:
            return
        self.driver.find_element_by_css_selector(item + ' ' + self.selectors_item['reference']).send_keys(Keys.ENTER)

    def get_price(self, number):
        try:
            item=self.__correct(number)
        except:
            return
        price=self.driver.find_element_by_css_selector(item + ' ' + self.selectors_item['price']).text
        price=price.replace(",",".").replace(" ","").replace(u"руб.","")
        return price
