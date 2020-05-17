from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址']"

    # 默认的姓名+电话
    name_and_phone_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认的标记
    default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    def click_new_address(self):
        self.click(self.new_address_button)

    def get_name_and_phone_text(self):
        return self.get_text(self.name_and_phone_text_view)

    def click_default(self):
        self.click(self.default_feature)

