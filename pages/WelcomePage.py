from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


class WelcomePage(BasePage):

    login_link_text = (AppiumBy.ID, "com.fivemobile.thescore:id/txt_sign_in")

    def __init__(self, driver):
        super(WelcomePage, self).__init__(driver)

    def login(self):
        login_link = self.defaultWait.until(EC.visibility_of_element_located(self.login_link_text))
        x = login_link.location['x'] + login_link.size['width'] * 0.9
        y = login_link.location['y'] + login_link.size['height'] / 2
        self.tap_at_coordinates(x, y)
