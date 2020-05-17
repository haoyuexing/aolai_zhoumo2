from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    nikename_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 加入vip
    vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    # 分类
    category_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tab_category' and @text='分类']"

    def get_nikename_text(self):
        return self.get_text(self.nikename_text_view)

    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()

    def click_vip(self):
        self.find_element_with_scroll(self.vip_button).click()

    def click_category(self):
        self.click(self.category_button)