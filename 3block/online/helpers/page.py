class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._search_result_route = None
        self._extras_group = None

    @property
    def search_bar(self):
        from online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def search_result_route(self):
        from online.helpers.search_result_route import SearchResultRoute

        if self._search_result_route is None:
            self._search_result_route = SearchResultRoute(self.driver, self.driver.find_element_by_css_selector(SearchResultRoute.selectors['self']))
        return self._search_result_route

    @property
    def extra_group(self):
        from online.helpers.extras_group import Extras_group
        if self._extras_group is None:
            self._extras_group = Extras_group(self.driver, self.driver.find_element_by_css_selector(Extras_group.selectors['self']))
        return self._extras_group

    def open(self, url):
        self.driver.get(url)

