from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()