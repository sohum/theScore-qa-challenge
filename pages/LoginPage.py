from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import json

class LoginPage(BasePage):

    email = (AppiumBy.ID, 'com.fivemobile.thescore:id/email_input_edittext')
    password = (AppiumBy.ID, 'com.fivemobile.thescore:id/password_input_edittext')
    login = (AppiumBy.ID, 'com.fivemobile.thescore:id/login_button')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_with_email(self):
        try:
            with open('../secrets.js') as f:
                data = json.load(f)
                email = data['email']
                password = data['password']
        except Exception as e:
            print("Error: ", e)

        self.type(self.email, email)
        self.type(self.password, password)
        self.tap(self.login)
        self.tap_modal_x()
