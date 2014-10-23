__author__ = 'Djonny'
from online.helpers.base_component import BaseComponent

class Extras_group(BaseComponent):

    selectors = {
        'self': '.extras',
        'download': '.extras__group:nth-of-type(1) .extras__btn._withText.extras__download',
        'share': '.extras__group:nth-of-type(2) .extras__btn.extras__share',
        'feedback': '.extras__group:nth-of-type(2) .extras__btn.extras__feedback',
        'more': '.extras__group:nth-of-type(2) .extras__btn.extras__more'
    }
    module_share=None

    share_clicked=False

    def share_click(self):
        from online.helpers.module_share import Module_Share
        if self.share_clicked == False:
            self.driver.find_element_by_css_selector(self.selectors['share']).click()
            self.share_clicked=True
        if self.module_share is None:
            self.module_share = Module_Share(self.driver, self.driver.find_element_by_css_selector(Module_Share.selectors['self']))

    def get_url_share(self):
        self.share_click()
        url=self.module_share.get_url()
        self.module_share.close_module()
        return url
