import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsListPage(BaseAction):

    # 商品的图片
    goods_image = By.ID, "com.yunmall.lc:id/iv_element_1"

    def click_random_goods_image(self):
        # 所有图片的元素的列表
        imageviews = self.find_elements(self.goods_image)
        # 所有图片的总数
        imageviews_count = len(imageviews)
        # 随机生成的一个总是范围之内的下标
        imageviews_random_index = random.randint(0, imageviews_count - 1)
        # 随机点击某个图片
        imageviews[imageviews_random_index].click()

