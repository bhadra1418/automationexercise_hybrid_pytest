import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.logger import get_logger
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_valid_user(self):
        logger = get_logger("TestLogin")
        home = HomePage(self.driver)
        home.click_signup_login()
        login = LoginPage(self.driver)
        login.login("testuser@example.com", "testpassword")
        login_text = self.driver.find_element(By.XPATH, "//a[contains(text(),'Your email or password is incorrect!')]").text
        assert "Your email or password is incorrect!" in login_text
        logger.info("Login test passed")
