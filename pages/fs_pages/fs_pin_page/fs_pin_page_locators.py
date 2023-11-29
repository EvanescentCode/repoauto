from utilities.locator_builder import LocatorBuilder


class FsLoginPageLocators:
    PIN_FIELD = LocatorBuilder.name("ctl00$CPH$Content__V_UZYTKOWNIK__Q__PIN")
    SUBMIT_PIN_BUTTON = LocatorBuilder.id("ctl00_CPH_Content__V_UZYTKOWNIK__Q__PIN_POTWIERDZ")