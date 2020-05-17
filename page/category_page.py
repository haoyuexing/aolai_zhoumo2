import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):
    # 分类页面 - 图片的特征
    category_image = By.ID, "com.yunmall.lc:id/iv_img"

    def click_random_category_image(self):
        # 所有图片的元素的列表
        imageviews = self.find_elements(self.category_image)
        # 所有图片的总数
        imageviews_count = len(imageviews)
        # 随机生成的一个总是范围之内的下标
        imageviews_random_index = random.randint(0, imageviews_count - 1)
        # 随机点击某个图片
        imageviews[imageviews_random_index].click()

