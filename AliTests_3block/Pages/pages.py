__author__ = 'Djonny'

class Pages():
    def __init__(self, driver):
        """
        :type in_driver: WebDriver
        """
        self.driver = driver
        self._search_bar_template=None
        self._page_main = None
        self._page_goods = None
        self._page_search_result = None
        self._page_cart = None

    @property
    def search_bar_template(self):
        from Pages.search_bar_template import SearchBarTemplate

        if self._search_bar_template is None:
            self._search_bar_template = SearchBarTemplate(self.driver, self.driver.find_element_by_css_selector(SearchBarTemplate.selectors['self']))
        return self._search_bar_template

    @property
    def page_main(self):
        from Page_Main.page_main import PageMain

        if self._page_main is None:
            self._page_main = PageMain(self.driver,self.search_bar_template)
        return self._page_main

    @property
    def page_goods(self):
        from Page_Goods.page_goods import PageGoods

        if self._page_goods is None:
            self._page_goods = PageGoods(self.driver,self.search_bar_template)
        return self._page_goods

    @property
    def page_search_result(self):
        from Page_Search_Result.page_search_result import PageSearchResult

        if self._page_search_result is None:
            self._page_search_result = PageSearchResult(self.driver,self.search_bar_template)
        return self._page_search_result

    @property
    def page_cart(self):
        from Page_Cart.page_cart import PageCart

        if self._page_cart is None:
            self._page_cart = PageCart(self.driver,self.search_bar_template)
        return self._page_cart

    def open(self,url):
        self.driver.get(url)

    def back(self):
        self.driver.back()