import os
import sys

sys.path.append(os.getcwd())

from day04 import page

from day04.base.base import Base


class PageLogin(Base):
    def page_click_me(self):
        self.base_click(page.login_me)

    def page_click_username_link(self):
        pass

    def page_input_username(self):
        pass

    def page_input_pwd(self):
        pass

    def page_click_login_btn(self):
        pass

    def page_get_info(self):
        pass

    def page_click_setting(self):
        pass

    def page_drag_and_drop(self):
        pass

    def page_click_logout_btn(self):
        pass

    def page_click_logout_btn_ok(self):
        pass
