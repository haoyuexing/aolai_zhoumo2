import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver()

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.reg_page = RegPage(self.driver)
        self.me_page = MePage(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 点击关闭
        self.home_page.click_close()
        # 点击我
        self.home_page.click_me()
        # 点击已有账号去登陆
        self.reg_page.click_login()
        # 输入用户名
        self.login_page.input_username(username)
        # 输入密码
        self.login_page.input_password(password)
        # 点击登录
        self.login_page.click_login()

        if toast is None:
            # 用用户名的形式断言
            assert self.me_page.get_nikename_text() == username
        else:
            # 用toast的形式断言
            assert self.login_page.is_toast_exist(toast)
