from base.base_driver import Page
from pages.fs_pages.fs_continue_process.fs_continue_process_locators import FsContinueProcessLocators as Locs


class FsContinueProcessPage(Page):
    def fill_and_go_next(self):
        self.continue_process()

    def continue_process(self):
        self.click(Locs.CONTINUE_PROCESS)

