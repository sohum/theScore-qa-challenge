from helpers.DriverManager import DriverManager
from pages.FavoritesPage import FavoritesPage
from pages.LeaguePage import LeaguePage
from pages.LoginPage import LoginPage
from pages.WelcomePage import WelcomePage
from pages.components.BottomNav import BottomNav
from pages.components.Toolbar import Toolbar
from behave import fixture, use_fixture


@fixture
def appium_driver(context):
    context.driver = DriverManager.get_driver()
    yield context.driver
    context.driver.quit()

def before_scenario(context, scenario):
    use_fixture(appium_driver, context)
    context.welcome_page = WelcomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.bottom_nav = BottomNav(context.driver)
    context.favorites_page = FavoritesPage(context.driver)
    context.league_page = LeaguePage(context.driver)
    context.toolbar = Toolbar(context.driver)
