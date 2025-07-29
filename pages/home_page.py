from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGNUP_LOGIN = (By.LINK_TEXT, "Signup / Login")

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN)
