from selenium import webdriver


class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        # There are the 3 locators on this page
        self.username_textbox_xpath = "//input[@id='txtUsername']"
        self.password_textbox_xpath = "//input[@id='txtPassword']"
        self.login_button_xpath = "//input[@id='btnLogin']"
        self.forgot_password_xpath = "//a[contains(text(),'Forgot your password?')]"
        self.orange_hrm_link_xpath = "//a[contains(text(),'OrangeHRM, Inc')]"
        self.select_options = "//select[@id='openIdProvider']"
        self.facebook_icon = "//a[2]//img[1]"
        self.twitter_icon = "//a[3]//img[1]"
        self.youtube_icon = "//a[4]//img[1]"
        self.linkedin_icon = "//a[1]//img[1]"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)
        #self.driver.implicity_wait(10)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        #self.driver.implicity_wait(10)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

