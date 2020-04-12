import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.page import Page
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)

        self.page = Page(self.driver)

        # self.home_page = HomePage(self.driver)
        # self.login_page = LoginPage(self.driver)
        # self.reg_page = RegPage(self.driver)
        # self.me_page = MePage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # def test_hello(self):
    #     # self.home_page.login_if_not(self.reg_page, self.login_page)
    #     self.page.home.login_if_not(self.page)

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 点击关闭
        self.page.home.click_close()
        # 点击我
        self.page.home.click_me()
        # 点击已有账号去登陆
        self.page.reg.click_login()
        # 输入用户名
        self.page.login.input_username(username)
        # 输入密码
        self.page.login.input_password(password)
        # 点击登录
        self.page.login.click_login()

        if toast is None:
            # 用用户名的形式断言
            assert self.page.me.get_nikename_text() == username
        else:
            # 用toast的形式断言
            assert self.page.login.is_toast_exist(toast)
