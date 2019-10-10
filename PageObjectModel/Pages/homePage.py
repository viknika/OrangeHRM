from selenium import webdriver

class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.marketplace_xpath = "//input[@id='MP_link']"
        self.welcome_admin_xpath = "//a[@id='welcome']"
        self.about_xpath = "//a[@id='aboutDisplayLink']"
        self.logout_xpath = "//a[contains(text(),'Logout')]"
        self.admin_xpath = "//b[contains(text(),'Admin')]"
        self.admin_user_manager_xpath = "//a[@id='menu_admin_UserManagement']"

    def welcome_button(self):
        self.driver.find_element_by_xpath(self.welcome_admin_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()



