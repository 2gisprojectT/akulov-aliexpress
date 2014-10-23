__author__ = 'Djonny'

from online.helpers.base_component import BaseComponent


class Module_Share(BaseComponent):

    selectors = {
        'self': '.share',
        'url_share': '.share .share__popup .share__popupUrl .share__popupUrlInput',
        'close': '.share .share__popupClose'
    }

    def get_url(self):
        return self.driver.find_element_by_css_selector(self.selectors['url_share']).get_attribute('value')

    def close_module(self):
        self.driver.find_element_by_css_selector(self.selectors['close']).click()