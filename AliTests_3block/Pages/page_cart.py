__author__ = 'Djonny'

class PageCart():
    def __init__(self,in_driver,sbt):
        """
        :type in_driver: WebDriver
        :type sbt: SearchBarTemplate
        """
        self.driver=in_driver
        self.search_bar_template= sbt
        self._added_goods = None

    @property
    def added_goods(self):
        from Components.added_goods import AddedGoods

        if self._added_goods is None:
            self._added_goods = AddedGoods(self.driver, self.driver.find_element_by_css_selector(AddedGoods.selectors['self']))
        return self._added_goods