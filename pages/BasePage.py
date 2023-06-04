from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    driver = webdriver
    default_wait = WebDriverWait
    dismiss_modal = (AppiumBy.ID, 'com.fivemobile.thescore:id/dismiss_modal')

    def __init__(self, driver):
        self.driver = driver
        time_out_in_seconds = 10
        self.defaultWait = WebDriverWait(self.driver, time_out_in_seconds)

    def tap(self, locator, custom_wait=10):
        wait = WebDriverWait(self.driver, custom_wait)
        wait.until(EC.visibility_of_element_located(locator)).click()

    def type(self, locator, value):
        el = self.defaultWait.until(EC.element_to_be_clickable(locator))
        el.send_keys(value)

    def tap_at_coordinates(self, x, y):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def tap_modal_x(self):
        self.defaultWait.until(EC.visibility_of_element_located(self.dismiss_modal)).click()

    def is_displayed(self, locator):
        try:
            self.defaultWait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            return False
