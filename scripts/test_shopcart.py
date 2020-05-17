import time

from base.base_driver import init_driver
from page.page import Page


class TestShopcart:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_add_shopcart(self):
        # 如果没有登录就登录，停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 - 点击分类
        self.page.me.click_category()
        # 分类 - 点击随机的一个商品分类
        self.page.category.click_random_category_image()
        # 商品列表 - 点击随机的一个商品
        self.page.goods_list.click_random_goods_image()
        # 商品详情 - 点击加入购物车
        self.page.goods_detail.click_add_shopcart()



