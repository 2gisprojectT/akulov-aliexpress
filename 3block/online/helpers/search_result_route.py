__author__ = 'Djonny'
from online.helpers.base_component import BaseComponent


class SearchResultRoute(BaseComponent):

    selectors = {
        'self': '.routeResults__wrap',
        'steps_route': '.routeResults__steps > li.routeResults__stepsItem'
    }


    @property
    def count_steps_route(self):
        return len(self.driver.find_elements_by_css_selector(self.selectors['steps_route']))
