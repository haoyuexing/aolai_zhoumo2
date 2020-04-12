from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10, poll_frequency=1):
        self.find_element(feature, timeout, poll_frequency).click()

    def clear(self, feature, timeout=10, poll_frequency=1):
        self.find_element(feature, timeout, poll_frequency).clear()

    def input(self, feature, text, timeout=10, poll_frequency=1):
        self.clear(feature, timeout, poll_frequency)
        self.find_element(feature, timeout, poll_frequency).send_keys(text)

    def get_text(self, feature, timeout=10, poll_frequency=1):
        return self.find_element(feature, timeout, poll_frequency).text




