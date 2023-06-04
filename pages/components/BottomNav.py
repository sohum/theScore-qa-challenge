from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class BottomNav(BasePage):

    favorites_btn = (AppiumBy.ACCESSIBILITY_ID, 'Favorites')

    def __init__(self, driver):
        super(BottomNav, self).__init__(driver)

    def favorites(self):
        self.tap(self.favorites_btn)
