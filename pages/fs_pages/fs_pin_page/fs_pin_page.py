from base.base_driver import Page
from pages.fs_pages.fs_pin_page.fs_pin_page_data import FsPinPageData
from pages.fs_pages.fs_pin_page.fs_pin_page_locators import FsLoginPageLocators as Locs


class FsPinPage(Page):
    def fill_and_go_next(self, pin: FsPinPageData):
        self.pin_field(pin.pin)
        self.submit_pin_button()

    def pin_field(self, pin: str):
        self.send_keys(Locs.PIN_FIELD, pin)

    def submit_pin_button(self):
        self.click(Locs.SUBMIT_PIN_BUTTON)
