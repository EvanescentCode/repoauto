import time

from utilities.locator_builder import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.__driver = driver

    def scroll(self):
        page_length = self.__driver.execute.script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return page_lenght"
        )
        match = False
        while (match == False):
            last_count = page_length
            time.sleep(2)
            lenght_of_page = self.__driver.execute.script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight; return page_lenght"
            )

        time.sleep(3)

    def back(self, amount=None):
        amount = amount if amount else 1
        for am in range(amount):
            self.__driver.back()

    def get(self, url):
        self.__driver.get(url)

    def find_element(self, locator: Locator) -> Locator:
        return self.__driver.find_element(locator.by, locator.value)

    def find_multiple_elements(self, locator: Locator) -> list[Locator]:
        return self.__driver.find_multiple_elements(locator.by, locator.value)

    def send_keys(self, locator: Locator, value: str):
        self.__driver.find_element(locator.by, locator.value).send_keys(value)

    def select_from_dropdown(self, locator: Locator, value: str):
        select = Select(self.__driver.find_element(locator.by, locator.value))
        select.select_by_value(value)

    def click(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).click()

    def submit(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).submit()

    def quit(self):
        self.__driver.quit()

    def get_page_title(self) -> str:
        return self.__driver.title

    def get_page_source(self) -> str:
        return self.__driver.page_source

    def switch_to_frame(self, locator: Locator):
        frame = self.find_element(locator)
        self.__driver.switch_to.frame(frame)

    def refresh(self):
        self.__driver.refresh()

    def switch_to_window(self, window_handle):
        self.__driver.switch_to.window(window_handle)

    def wait_for_appearance(self, locator: Locator, timeout: int = 10) -> Locator:
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(EC.presence_of_all_elements_located((locator.by, locator.value)))
        return element

    def wait_for_item_to_be_clickable(self, locator: Locator, timeout: int = 10) -> Locator:
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(EC.element_to_be_clickable((locator.by, locator.value)))
        return element

    def wait_for_presence_of_all_elements_located(self, locator: Locator, timeout: int = 10) -> Locator:
        wait = WebDriverWait(self.__driver, timeout)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator.by, locator.value)))
        return list_of_elements

    def long_wait_for_item_to_be_clickable(self, locator: Locator, timeout: int = 120) -> Locator:
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(EC.element_to_be_clickable((locator.by, locator.value)))
        return element

    def visibility_of_item(self, locator: Locator, timeout: int = 120) -> Locator:
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(EC.visibility_of_element_located((locator.by, locator.value)))
        return element

    def get_text(self, locator: Locator) -> str:
        return self.__driver.find_element(locator.by, locator.value).text
