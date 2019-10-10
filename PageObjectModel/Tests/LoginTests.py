import unittest
import time
from selenium import  webdriver
from UnitTesting.PageObjectModel.Pages.loginPage import LoginPage
from UnitTesting.PageObjectModel.Pages.homePage import HomePage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:\Downloads\chromedriver.exe")
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.welcome_button()
        homepage.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
