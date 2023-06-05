from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC


class LeaguePage(BasePage):

    league_title = (AppiumBy.ID, 'com.fivemobile.thescore:id/titleTextView')

    def __init__(self, driver):
        super(LeaguePage, self).__init__(driver)

    def get_league_title(self):
        return self.defaultWait.until(EC.visibility_of_element_located(self.league_title)).text

    def tab(self, tab_name):
        tab = (AppiumBy.ACCESSIBILITY_ID, "{}".format(tab_name))
        self.tap(tab)

    def is_tab_selected(self, tab_name):
        tab = (AppiumBy.ACCESSIBILITY_ID, "{}".format(tab_name))
        return self.is_selected(tab)

    def is_team_displayed(self, team_name):
        team = (AppiumBy.XPATH,
             "//android.widget.TextView[contains(@text, \"{}\")]".format(team_name))
        return self.is_displayed(team)
