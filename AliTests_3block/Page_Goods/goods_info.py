#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from Pages.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys

class GoodsInfo(BaseComponent):

    selectors = {
        'self': '.main-wrap.util-clearfix',
        'goods_name': '.product-name',
        'quantity': '#product-info-txt-quantity',
        'quantity_left': '#quantity-no',
        'price': '.total-price',
        'button_buy_now': '#buy-now',
        'button_add_to_cart': '#add-to-cart',
        'choice_go_to_page_goods': 'button.ui-button.ui-button-normal.ui-button-medium',
        'choice_go_to_page_cart': 'a.ui-button.ui-button-normal.ui-button-medium'
    }

    def get_goods_name(self):
        return self.driver.find_element_by_css_selector(self.selectors['goods_name']).text

    def get_quantity_left(self):
        mass=self.driver.find_elements_by_css_selector(self.selectors['quantity_left'])
        if len(mass) != 0:
            return int(mass[0].text)
        else: return False

    def get_quantity(self):
        return self.driver.find_element_by_css_selector(self.selectors['quantity']).get_attribute('value')

    def set_quantity(self,quantity):
        res=self.get_quantity_left()
        if res != False:
            if res < quantity:
                quantity=res
        qua=self.driver.find_element_by_css_selector(self.selectors['quantity'])
        qua.send_keys(Keys.BACKSPACE)
        qua.send_keys(quantity)


    def get_price(self):
        price=self.driver.find_element_by_css_selector(self.selectors['price']).text
        price=price.replace(",",".").replace(" ","").replace(u"руб.","")
        return float(price)

    def button_buy_now_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_buy_now']).click()

    def button_add_to_cart_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_add_to_cart']).click()

    def choice_go_to_page_goods(self):
        self.driver.find_element_by_css_selector(self.selectors['choice_go_to_page_goods']).click()

    def choice_go_to_page_cart(self):
        self.driver.find_element_by_css_selector(self.selectors['choice_go_to_page_cart']).click()