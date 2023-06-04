from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(BasePage):

    email = (AppiumBy.ID, 'com.fivemobile.thescore:id/email_input_edittext')
    password = (AppiumBy.ID, 'com.fivemobile.thescore:id/password_input_edittext')
    login = (AppiumBy.ID, 'com.fivemobile.thescore:id/login_button')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_with_email(self, email, password):
        self.type(self.email, email)
        self.type(self.password, password)
        self.tap(self.login)
        self.tap_modal_x()
