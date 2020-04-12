from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # 首页 - 关闭更新按钮
    close_button = By.ID, "com.yunmall.lc:id/img_close"


    # 首页 - 我
    me_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tab_me' and @text='我']"

    # 点击 - 关闭更新按钮
    def click_close(self):
        self.click(self.close_button)

    # 点击 - 我
    def click_me(self):
        self.click(self.me_button)

    def login_if_not(self, page):
        """
        调用完成之后会停留在 "我" 的页面
        :param reg_page:
        :param login_page:
        :return:
        """
        self.click_close()
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 点击已有账号去登陆
        page.reg.click_login()
        # 输入用户名
        page.login.input_username("itfeat")
        # 输入密码
        page.login.input_password("itfeat123000")
        # 点击登录
        page.login.click_login()



