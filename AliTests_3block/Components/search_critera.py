#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from selenium.webdriver.common.keys import Keys

from Components.base_component import BaseComponent


class SearchCriteria(BaseComponent):

    selectors = {
        'self': '.narrow-down-area',
        'input_words': '#ipt-kwd',
        'input_price_from': '#filter-price-from',
        'input_price_to': '#filter-price-to',
        'input_quantity_from': '#filter-quantity-from',
        'input_quantity_to': '#filter-quantity-to',
        'country_selector': '#country-selector',
        'country_container': '#country-container',
        'button_free_ship': '#linkFreeShip',
        'button_favorite': '#linkFavorite',
        'button_only_piece': '#linkRtl',
        'button_sale': '#linkOnSale',
        'button_seller_online': '#linkAtmOnline'

    }

    #Ключевое слово
    def criteria_words(self, query):
        inputwords=self.driver.find_element_by_css_selector(self.selectors['input_words'])
        inputwords.send_keys(query)
        inputwords.send_keys(Keys.ENTER)

    def get_str_criteria_words(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_words']).get_attribute('value')

    #Границы цены
    def criteria_price(self, price_from, price_to):
        self.driver.find_element_by_css_selector(self.selectors['input_price_from']).send_keys(price_from)
        price=self.driver.find_element_by_css_selector(self.selectors['input_price_to'])
        price.send_keys(price_to)
        price.send_keys(Keys.ENTER)

    def get_str_criteria_price_from(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_price_from']).get_attribute('value')

    def get_str_criteria_price_to(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_price_to']).get_attribute('value')

    #Границы количества
    def criteria_quantity(self, quantity_from, quantity_to):
        self.driver.find_element_by_css_selector(self.selectors['input_quantity_from']).send_keys(quantity_from)
        quantity=self.driver.find_element_by_css_selector(self.selectors['input_quantity_to'])
        quantity.send_keys(quantity_to)
        quantity.send_keys(Keys.ENTER)

    def get_str_criteria_quantity_from(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_quantity_from']).get_attribute('value')

    def get_str_criteria_quantity_to(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_quantity_to']).get_attribute('value')

    #Кнопки
    def free_ship_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_free_ship']).send_keys(Keys.ENTER)

    def favorite_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_favorite']).send_keys(Keys.ENTER)

    def only_piece_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_only_piece']).send_keys(Keys.ENTER)

    def sale_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_sale']).send_keys(Keys.ENTER)

    def seller_online_click(self):
        self.driver.find_element_by_css_selector(self.selectors['button_seller_online']).send_keys(Keys.ENTER)