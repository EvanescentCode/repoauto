from base.base_driver import Page
from pages.fs_pages.fs_menu_page.fs_menu_page_locators import FsMenuPageLocators as Locs


class FsMenuPage(Page):
    def fill_and_go_next(self):
        self.create_new_form()

    def create_new_form(self):
        self.click(Locs.CREATE_NEW_FORM_BUTTON)
