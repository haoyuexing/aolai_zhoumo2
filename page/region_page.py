import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegionPage(BaseAction):

    # title
    city_feature = By.ID, "com.yunmall.lc:id/area_title"

    def choose_region(self):
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            cities = self.find_elements(self.city_feature)
            cities_count = len(cities)
            cities_index = random.randint(0, cities_count - 1)
            cities[cities_index].click()
            time.sleep(1)
