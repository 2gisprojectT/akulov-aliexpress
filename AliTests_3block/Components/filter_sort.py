__author__ = 'Djonny'

from selenium.webdriver.common.keys import Keys

from Components.base_component import BaseComponent


class FilterSort(BaseComponent):

    selectors = {
        'self': '.view-filter',
        'best_match': '.narrow-down-bg:nth-of-type(3) > a',
        'orders': '.narrow-down-bg:nth-of-type(4) > a',
        'new': '.narrow-down-bg:nth-of-type(5) > a',
        'seller_rating': '.narrow-down-bg:nth-of-type(6) > a',
        'price': '.narrow-down-bg:nth-of-type(7) > a'

    }

    def sort_result_by_best_match(self):
        self.driver.find_element_by_css_selector(self.selectors['best_match']).send_keys(Keys.ENTER)

    def sort_result_by_orders(self):
        self.driver.find_element_by_css_selector(self.selectors['orders']).send_keys(Keys.ENTER)

    def sort_result_by_new(self):
        self.driver.find_element_by_css_selector(self.selectors['new']).send_keys(Keys.ENTER)

    def sort_result_by_seller_rating(self):
        self.driver.find_element_by_css_selector(self.selectors['seller_rating']).send_keys(Keys.ENTER)

    def sort_result_by_price(self):
        self.driver.find_element_by_css_selector(self.selectors['price']).send_keys(Keys.ENTER)
