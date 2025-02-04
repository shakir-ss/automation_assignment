from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config import PIN, URL


class LoginPage(BasePage):
    PIN_INPUT = (By.ID, "access-code")
    LOGIN_BUTTON = (By.ID, "sign-in-button")

    def navigate(self):
        self.driver.get(URL)

    def login(self):
        self.enter_text(self.PIN_INPUT, PIN)
        self.click(self.LOGIN_BUTTON)
