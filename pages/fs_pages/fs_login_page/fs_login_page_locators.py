from utilities.locator_builder import LocatorBuilder


class FsLoginPageLocators:
    LOGIN_FIELD = LocatorBuilder.name("ctl00$CPH$Content__V_UZYTKOWNIK__Q__LOGIN")
    LOGIN_BUTTON = LocatorBuilder.id("ctl00_CPH_Content__V_UZYTKOWNIK__Q__ZALOGUJ")