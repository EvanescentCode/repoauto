from base.base_driver import Page
from pages.fs_pages.fs_login_page.fs_login_page_data import FsLoginPageData
from pages.fs_pages.fs_login_page.fs_login_page_locators import FsLoginPageLocators as Locs


class FsLoginPage(Page):
    def fill_and_go_next(self, login: FsLoginPageData):
        self.login_field(login.login)
        self.login_button()

    def login_field(self, login: str):
        self.send_keys(Locs.LOGIN_FIELD, login)

    def login_button(self):
        self.click(Locs.LOGIN_BUTTON)
