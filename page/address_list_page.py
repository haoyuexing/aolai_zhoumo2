from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址']"

    # 默认的姓名+电话
    name_and_phone_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认的标记
    default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 删除按钮
    delete_button = By.XPATH, "//*[@text='删除']"

    # 确认按钮
    commit_button = By.XPATH, "//*[@text='确认']"

    def click_new_address(self):
        self.click(self.new_address_button)

    def get_name_and_phone_text(self):
        return self.get_text(self.name_and_phone_text_view)

    def click_default(self):
        self.click(self.default_feature)

    def click_edit(self):
        self.click(self.edit_button)

    def click_delete(self):
        self.click(self.delete_button)

    def click_commit(self):
        self.click(self.commit_button)

    def is_default_exist(self):
        return self.is_feature_exist(self.default_feature)

    def delete_all_address(self):
        for i in range(10):
            # 点击编辑
            self.click_edit()
            try:
                # 点击删除
                self.click_delete()
            except Exception as e:
                return
            # 点击确认
            self.click_commit()

    # 第二种删除十次地址的方法
    # def delete_all_address(self):
    #     for i in range(10):
    #         # 点击编辑
    #         self.click_edit()
    #         # 点击删除
    #         self.click_delete()
    #         # 点击确认
    #         self.click_commit()
    #
    #         # 没删除一次判断是否有"默认"，如果有继续删除，如果没有则结束这个方法
    #         if not self.is_feature_exist(self.default_feature):
    #             return
