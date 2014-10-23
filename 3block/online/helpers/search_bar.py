from online.helpers.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys
import time
class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'input_from': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'input_to': '.searchBar__form .searchBar__textfield._to .suggest__input',
        'submit_route': '.searchBar__submit._rs',
        'tab_search': '.searchBar__tab.searchBar__refbookTab',
        'tab_route_search': '.searchBar__tab.searchBar__rsTab'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['tab_search']).click()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def get_str_search(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')

    def search_route(self, str_from, str_to):
        self.driver.find_element_by_css_selector(self.selectors['tab_route_search']).click()
        self.driver.find_element_by_css_selector(self.selectors['input_from']).send_keys(str_from)
        self.driver.find_element_by_css_selector(self.selectors['input_to']).send_keys(str_to)
        self.driver.find_element_by_css_selector(self.selectors['submit_route']).submit()

    def get_str_search_from(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_from']).get_attribute('value')

    def get_str_search_to(self):
        return self.driver.find_element_by_css_selector(self.selectors['input_to']).get_attribute('value')