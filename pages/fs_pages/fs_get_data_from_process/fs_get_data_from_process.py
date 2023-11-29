import re
import logging
from base.base_driver import Page
from pages.fs_pages.fs_get_data_from_process.fs_get_data_from_process_locators import FsGetDataFromProcessLocators
from utilities.utils import Utils


class FsGetDataFromProcess(Page):
    log = Utils.custom_logger(logging.DEBUG)

    def fill_and_go_next(self):
        self.get_fkt_from_process()
        self.get_uid_from_process()
        self.resignation_button()

    def get_fkt_from_process(self):
        fkt = self.get_text(FsGetDataFromProcessLocators.GET_FKT_FROM_PROCESS)
        match = re.search(r'value="([^"]+)"', fkt)
        if match:
            value = match.group(1)
            self.log(value)
        else:
            print("Nie znaleziono wartości.")

    def get_uid_from_process(self):
        uid = self.get_text(FsGetDataFromProcessLocators.GET_UID_FROM_PROCESS)
        match = re.search(r"uid=([a-f0-9-]+)", uid)
        if match:
            uid_value = match.group(1)
            self.log(uid_value)
        else:
            print("Nie znaleziono wartości UID.")

    def resignation_button(self):
        self.click(FsGetDataFromProcessLocators.RESIGNATION_BUTTON)
