from base.base_driver import Page
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_data import FsCustomerAcquisitionPageData
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_enum import FsCustomerAcquisitionEnum
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_locators import \
    FsCustomerAcquisitionLocators as Locs


class FsCustomerAcquisitionPage(Page):
    def fill_and_go_next(self, acquisition: FsCustomerAcquisitionPageData):
        self.customer_acquisition()
        self.select_acquisition(acquisition.acquisition.online)
        self.next_button()

    def customer_acquisition(self):
        self.click(Locs.CUSTOMER_ACQUISITION_DROPDOWN)

    def select_acquisition(self, acquisition: str):
        self.select_from_dropdown(Locs.CUSTOMER_ACQUISITION_DROPDOWN, acquisition)

    def next_button(self):
        self.click(Locs.NEXT_BUTTON)
