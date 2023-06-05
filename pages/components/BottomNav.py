from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class BottomNav(BasePage):

    def __init__(self, driver):
        super(BottomNav, self).__init__(driver)

    def tab(self, tab_name):
        tab = (AppiumBy.ACCESSIBILITY_ID, "{}".format(tab_name))
        self.tap(tab, 15)
