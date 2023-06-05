from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class Toolbar(BasePage):

    back_btn = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')

    def __init__(self, driver):
        super(Toolbar, self).__init__(driver)

    def back(self):
        self.tap(self.back_btn)
