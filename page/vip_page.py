import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    code_edit_text = By.XPATH, "//*[@placeholder='邀请码必填']"

    vip_button = By.XPATH, "//*[@value='立即成为会员']"

    def input_code(self, text):
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.input(self.code_edit_text, text)
        self.driver.switch_to.context("NATIVE_APP")

    def click_vip(self):
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.click(self.vip_button)
        self.driver.switch_to.context("NATIVE_APP")