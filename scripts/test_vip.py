import time

from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import init_driver
from page.page import Page


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_vip(self):
        # 如果没有登录就登录，停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击 加入vip
        self.page.me.click_vip()

        time.sleep(2)
        print(self.driver.contexts)

        # vip - 输入 邀请码
        self.page.vip.input_code("hello")
        # vip - 点击 成为会员
        self.page.vip.click_vip()

        # 断言 邀请码输入不正确 是否在 page_source中
        assert self.page.vip.is_keyword_in_page_source("邀请码输入不正确")









