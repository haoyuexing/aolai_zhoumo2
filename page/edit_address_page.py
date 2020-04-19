from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    # 收件人
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    # 手机号
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    # 详细地址
    detail_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    # 邮编
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    # 设置默认地址
    default_button = By.ID, "com.yunmall.lc:id/address_default"
    # 所在地区
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 保存
    save_button = By.XPATH, "//*[@text='保存']"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    def input_detail(self, text):
        self.input(self.detail_edit_text, text)

    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)

    def click_default(self):
        self.click(self.default_button)

    def click_region(self):
        self.click(self.region_button)

    def click_save(self):
        self.click(self.save_button)


