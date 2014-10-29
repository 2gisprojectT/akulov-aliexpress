__author__ = 'Djonny'



class PageMain():
    def __init__(self,in_driver,sbt):
        """
        :type in_driver: WebDriver
        :type sbt: SearchBarTemplate
        """
        self.driver=in_driver
        self.search_bar_template= sbt

