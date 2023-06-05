from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


class FavoritesPage(BasePage):

    chips = (AppiumBy.ID, 'com.fivemobile.thescore:id/chips_container')

    def __init__(self, driver):
        super(FavoritesPage, self).__init__(driver)

    def is_page_displayed(self):
        return self.is_displayed(self.chips)

    def select_chip(self, chip_name):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text = \"{}\"]/parent::android.view.ViewGroup".format(chip_name)))).click()
