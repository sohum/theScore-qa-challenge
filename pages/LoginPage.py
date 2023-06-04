from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import json, os

class LoginPage(BasePage):

    email = (AppiumBy.ID, 'com.fivemobile.thescore:id/email_input_edittext')
    password = (AppiumBy.ID, 'com.fivemobile.thescore:id/password_input_edittext')
    login = (AppiumBy.ID, 'com.fivemobile.thescore:id/login_button')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_with_email(self):
        absolute_path = os.path.dirname(__file__)
        secrets_relative_path = '../secrets.js'
        secrets_full_path = os.path.join(absolute_path, secrets_relative_path)
        try:
            with open(secrets_full_path) as f:
                data = json.load(f)
                email = data['email']
                password = data['password']
        except Exception as e:
            print("Error: ", e)

        self.type(self.email, email)
        self.type(self.password, password)
        self.tap(self.login)
        self.tap_modal_x()
