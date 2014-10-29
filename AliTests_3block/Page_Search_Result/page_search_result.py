__author__ = 'Djonny'

class PageSearchResult():
    def __init__(self,in_driver,sbt):
        """
        :type in_driver: WebDriver
        :type sbt: SearchBarTemplate
        """
        self.driver=in_driver
        self.search_bar_template= sbt
        self._search_criteria = None
        self._filter_sort = None
        self._result_list_goods = None

    @property
    def search_criteria(self):
        from Page_Search_Result.search_critera import SearchCriteria

        if self._search_criteria is None:
            self._search_criteria = SearchCriteria(self.driver, self.driver.find_element_by_css_selector(SearchCriteria.selectors['self']))
        return self._search_criteria

    @property
    def filter_sort(self):
        from Page_Search_Result.filter_sort import FilterSort

        if self._filter_sort is None:
            self._filter_sort = FilterSort(self.driver, self.driver.find_element_by_css_selector(FilterSort.selectors['self']))
        return self._filter_sort

    @property
    def result_list_goods(self):
        from Page_Search_Result.result_list_goods import Result_list_goods

        if self._result_list_goods is None:
            self._result_list_goods = Result_list_goods(self.driver, self.driver.find_element_by_css_selector(Result_list_goods.selectors['self']))
        return self._result_list_goods