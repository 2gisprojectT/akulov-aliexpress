#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from Pages.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys


class AddedGoods(BaseComponent):

    selectors = {
        'self': '#page',
        'count': '.main-title-text-num',
        'item': '.item-group-wrapper',
        'total_price': '.total-price.ui-cost > b'
    }

    selectors_item={
        'reference': '.lnk-product-name',
        'quantity': '.product-quantity-input.ui-textfield.ui-textfield-system',
        'price': '.product-price .value',
        'total_price': '.product-price-total.ui-cost > b',
        'remove': '.remove-single-product'

    }



    @property
    def count(self):
        countmass=self.driver.find_elements_by_css_selector(self.selectors['count'])
        if len(countmass) == 0:
            return 0
        else:
            countstr=countmass[0].text.replace(u" товар","").replace(u"а(ов)","")
            return int(countstr)

    def get_total_price(self):
        if self.count != 0:
                tp=self.driver.find_element_by_css_selector(self.selectors['total_price'])
                return float(tp.text.replace(",",".").replace(" ","").replace(u"руб.",""))
        else: return -1
    def is_item(self,number):
        mass=self.driver.find_elements_by_css_selector(self.selectors['item'])
        if (len(mass)+1) < number:
            return False
        else: return True

    def get_price_item(self,number):
        if self.is_item(number):
            pricestr=self.driver.find_element_by_css_selector(self.selectors['item']+':nth-of-type('+str(number+2)+')'+' '+self.selectors_item['price'])
            return float(pricestr.text.replace(",",".").replace(" ","").replace(u"руб.",""))
        else: return -1

    def get_total_price_item(self,number):
        if self.is_item(number):
            totalpricestr=self.driver.find_element_by_css_selector(self.selectors['item']+':nth-of-type('+str(number+2)+')'+' '+self.selectors_item['total_price'])
            return float(totalpricestr.text.replace(",",".").replace(" ","").replace(u"руб.",""))
        else: return -1

    def get_quantity_item(self,number):
        if self.is_item(number):
            quantitystr=self.driver.find_element_by_css_selector(self.selectors['item']+':nth-of-type('+str(number+2)+')'+' '+self.selectors_item['quantity'])
            return int(quantitystr.get_attribute('value'))
        else: return -1

    def go_to_page_goods(self,number):
        if self.is_item(number):
            ref=self.driver.find_element_by_css_selector(self.selectors['item']+':nth-of-type('+str(number+2)+')'+' '+self.selectors_item['reference'])
            ref.click()
            return True
        else: return False

    def remove_goods(self,number):
        if self.is_item(number):
            self.driver.find_element_by_css_selector(self.selectors['item']+':nth-of-type('+str(number+2)+')'+' '+self.selectors_item['remove']).click()
            return True
        else: return False


