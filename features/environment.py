from helpers.DriverManager import DriverManager
from pages.FavoritesPage import FavoritesPage
from pages.LeaguePage import LeaguePage
from pages.LoginPage import LoginPage
from pages.WelcomePage import WelcomePage
from pages.components.BottomNav import BottomNav
from pages.components.Toolbar import Toolbar


def before_all(context):
    context.driver = DriverManager.get_driver()
    context.precondition_cache = set()
    context.welcome_page = WelcomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.bottom_nav = BottomNav(context.driver)
    context.favorites_page = FavoritesPage(context.driver)
    context.league_page = LeaguePage(context.driver)
    context.toolbar = Toolbar(context.driver)

def before_scenario(context, scenario):
    if "the user is logged in" in context.precondition_cache:
        context.driver.execute_script("mobile: activateApp", {"appId": "com.fivemobile.thescore"})

def after_scenario(context, scenario):
    context.driver.execute_script("mobile: terminateApp", {"appId": "com.fivemobile.thescore", "timeout": 3000})

def after_all(context):
    context.driver.quit()
