from page.about_page import AboutPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.reg_page import RegPage
from page.setting_page import SettingPage
from page.vip_page import VipPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def reg(self):
        return RegPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def vip(self):
        return VipPage(self.driver)