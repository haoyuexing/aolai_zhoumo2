from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # 首页 - 关闭更新按钮
    close_button = By.ID, "com.yunmall.lc:id/img_close"


    # 首页 - 我
    me_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tab_me' and @text='我']"

    # 点击 - 关闭更新按钮
    def click_close(self):
        self.click(self.close_button)

    # 点击 - 我
    def click_me(self):
        self.click(self.me_button)
