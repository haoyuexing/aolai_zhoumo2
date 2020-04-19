from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ScrollDirection:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).click()

    def clear(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).clear()

    def input(self, feature, text, timeout=10.0, poll_frequency=1.0):
        self.clear(feature, timeout, poll_frequency)
        self.find_element(feature, timeout, poll_frequency).send_keys(text)

    def get_text(self, feature, timeout=10.0, poll_frequency=1.0):
        return self.find_element(feature, timeout, poll_frequency).text

    def is_toast_exist(self, text, timeout=3, poll_frequency=0.1):
        # 用toast断言
        try:
            self.find_element((By.XPATH, "//*[contains(@text,'%s')]" % text), timeout, poll_frequency)
            return True
        except Exception as e:
            return False

    def get_toast_text(self, text, timeout=3, poll_frequency=0.1):
        try:
            element = self.find_element((By.XPATH, "//*[contains(@text,'%s')]" % text), timeout, poll_frequency)
            return element.txt
        except Exception as e:
            raise Exception("关键词为 %s 的toast不存在，请检查参数" % text)

    def scroll_page_one_time(self, direction=ScrollDirection.DOWN):
        """
        direction：滑动的方向
            down：从下往上
            up：从上往下
            left：从左往右
            right：从右往左
        :param direction:
        :return:
        """

        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        bottom_x = center_x
        bottom_y = screen_height * 0.75
        top_x = center_x
        top_y = screen_height * 0.25
        left_x = screen_height * 0.25
        left_y = center_y
        right_x = screen_height * 0.75
        right_y = center_y

        if direction == ScrollDirection.DOWN:
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == ScrollDirection.UP:
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == ScrollDirection.LEFT:
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        elif direction == ScrollDirection.RIGHT:
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        else:
            raise Exception("参数有误，请检查参数，应为：up/down/left/right")

    def find_element_with_scroll(self, feature, direction=ScrollDirection.DOWN):
        page_source = ""

        while True:

            try:

                if self.driver.page_source == page_source:
                    print("到底了，没有找到相关内容")
                    break
                page_source = self.driver.page_source

                return self.find_element(feature)
            except:
                self.scroll_page_one_time(direction)
