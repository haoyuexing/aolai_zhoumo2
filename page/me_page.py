from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    nikename_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    def get_nikename_text(self):
        return self.get_text(self.nikename_text_view)