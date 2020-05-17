from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):

    # 加入购物车
    add_shopcart_button = By.XPATH, "//*[@text='加入购物车']"

    def click_add_shopcart(self):
        self.click(self.add_shopcart_button)
