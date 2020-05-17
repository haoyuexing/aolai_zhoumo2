import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestClearCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("address_data", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        detail = args["detail"]
        post_code = args["post_code"]
        toast = args["toast"]

        # 如果没有登录就登录，停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 设置
        self.page.me.click_setting()
        # 设置 - 点击 地址管理
        self.page.setting.click_address()
        # 地址列表 - 点击 新增地址
        self.page.address_list.click_new_address()
        # 新增地址 - 输入 收件人
        self.page.edit_address.input_name(name)
        # 新增地址 - 输入 手机号
        self.page.edit_address.input_phone(phone)
        # 新增地址 - 输入 详细地址
        self.page.edit_address.input_detail(detail)
        # 新增地址 - 输入 邮编
        self.page.edit_address.input_post_code(post_code)
        # 新增地址 - 点击 设为默认地址
        self.page.edit_address.click_default()

        # 新增地址 - 点击 所在区域
        self.page.edit_address.click_region()
        # 区域选择 - 选择省市区
        self.page.region.choose_region()

        # 编辑地址 - 点击 保存
        self.page.edit_address.click_save()

        if toast is None:
            assert self.page.address_list.get_name_and_phone_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)

            # 收件人姓名2-15个字符
            # 收件人姓名2–15个字符
