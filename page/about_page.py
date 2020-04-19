from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    update_button = By.XPATH, "//*[@text='版本更新']"

    update_now_button = By.XPATH, "//*[@text='立即更新']"

    def is_update_now_exist(self):
        return self.is_feature_exist(self.update_now_button)

    def click_update(self):
        self.click(self.update_button)