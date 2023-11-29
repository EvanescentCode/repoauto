from selenium import webdriver
from pytest import fixture
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_enum import FsCustomerAcquisitionEnum
from pages.fs_pages.fs_dataclasses import FsPageDataclass
from pages.fs_pages.path import Paths
from testcases.common_path import CommonPath
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities.json_formatter import load_test_data


@fixture(autouse=True)
def test_data_01():
    return load_test_data(dataclass=FsPageDataclass, path=Paths.test_data("test_data01"))


class TestFsGetDataFromProcessPage:
    @fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://test2.falcon.nest.corp/FMBewnioseknew/WizardWfB.aspx?b=1&p=2&s=503&bankId=1&profileId=2&WebSite=2&c=1")
        yield
        self.driver.quit()

    def test_get_data_from_process(self, test_data_01, data: FsPageDataclass):
        CommonPath(self.driver).test_get_data_from_process(data)
