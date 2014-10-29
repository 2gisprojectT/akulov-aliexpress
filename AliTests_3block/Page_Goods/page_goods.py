__author__ = 'Djonny'

class PageGoods():
    def __init__(self,in_driver,sbt):
        """
        :type in_driver: WebDriver
        :type sbt: SearchBarTemplate
        """
        self.driver=in_driver
        self.search_bar_template= sbt
        self._goods_info = None

    @property
    def goods_info(self):
        from Page_Goods.goods_info import GoodsInfo

        if self._goods_info is None:
            self._goods_info = GoodsInfo(self.driver, self.driver.find_element_by_css_selector(GoodsInfo.selectors['self']))
        return self._goods_info