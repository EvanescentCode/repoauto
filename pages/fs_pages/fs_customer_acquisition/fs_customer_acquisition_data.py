from dataclasses import dataclass

from pages.fs_pages.fs_customer_acquisition.fs_customer_acquisition_enum import FsCustomerAcquisitionEnum


@dataclass
class FsCustomerAcquisitionPageData:
    acquisition: FsCustomerAcquisitionEnum = FsCustomerAcquisitionEnum.online
