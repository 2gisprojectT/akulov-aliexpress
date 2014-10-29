#-*- coding:UTF-8 -*-
__author__ = 'Djonny'

from Pages.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys

class SearchBarTemplate(BaseComponent):

    selectors = {
        'self': '.hm-middle',
        'input': 'input.search-key',
        'submit': 'input.search-button',
        'shop_cart': '.nav-cart.ru-nav-cart > a',
        'wish_list': '.nav-wishlist.ru-nav-wishlist > a',
        'login': '.nu-info-sign-top',
        'registration': '.nu-info-join',
        'log_out': '.nu-signout >p>a'
    }

    #На после авторизации не забыть изменить значение на True
    logged=False

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def get_str_search(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')

    def go_to_shop_cart(self):
        self.driver.find_element_by_css_selector(self.selectors['shop_cart']).send_keys(Keys.ENTER)

    def go_to_wish_list(self):
        self.driver.find_element_by_css_selector(self.selectors['wish_list']).send_keys(Keys.ENTER)

    def go_to_login_page(self):
        if self.logged == False:
            self.driver.find_element_by_css_selector(self.selectors['login']).send_keys(Keys.ENTER)

    def go_to_registration_page(self):
        if self.logged == False:
            self.driver.find_element_by_css_selector(self.selectors['registration']).send_keys(Keys.ENTER)

    def log_out(self):
        if self.logged == True:
            self.logged=False
            self.driver.find_element_by_css_selector(self.selectors['log_out']).send_keys(Keys.ENTER)