from base.base_driver import Page
from pages.fs_pages.fs_continue_process.fs_continue_process import FsContinueProcessPage
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition import FsCustomerAcquisitionPage
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_data import FsCustomerAcquisitionPageData
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_enum import FsCustomerAcquisitionEnum
from pages.fs_pages.fs_dataclasses import FsPageDataclass
from pages.fs_pages.fs_get_data_from_process.fs_get_data_from_process import FsGetDataFromProcess
from pages.fs_pages.fs_login_page.fs_login_page import FsLoginPage
from pages.fs_pages.fs_login_page.fs_login_page_data import FsLoginPageData
from pages.fs_pages.fs_menu_page.fs_menu_page import FsMenuPage
from pages.fs_pages.fs_pin_page.fs_pin_page import FsPinPage
from pages.fs_pages.fs_pin_page.fs_pin_page_data import FsPinPageData


class CommonPath:

    def __init__(self, driver):
        self.driver = driver
        self.screen_0 = FsLoginPage(self.driver)
        self.screen_1 = FsPinPage(self.driver)
        self.screen_2 = FsMenuPage(self.driver)
        self.screen_3 = FsCustomerAcquisitionPage(self.driver)
        self.screen_4 = FsContinueProcessPage(self.driver)
        self.screen_5 = FsGetDataFromProcess(self.driver)

    def test_get_data_from_process(self, data: FsPageDataclass):
        self.screen_0.fill_and_go_next(login=data.login)
        self.screen_1.fill_and_go_next(pin=data.pin)
        self.screen_2.fill_and_go_next()
        self.screen_3.fill_and_go_next(acquisition=data.acquisition.online)
        self.screen_4.fill_and_go_next()
        self.screen_5.fill_and_go_next()
