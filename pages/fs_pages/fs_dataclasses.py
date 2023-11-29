from dataclasses import dataclass
from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_data import FsCustomerAcquisitionPageData
from pages.fs_pages.fs_login_page.fs_login_page_data import FsLoginPageData
from pages.fs_pages.fs_pin_page.fs_pin_page_data import FsPinPageData


@dataclass
class FsPageDataclass:
    login: FsLoginPageData
    pin: FsPinPageData
    acquisition: FsCustomerAcquisitionPageData
