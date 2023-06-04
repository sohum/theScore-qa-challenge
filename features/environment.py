from helpers.DriverManager import DriverManager
from pages.FavoritesPage import FavoritesPage
from pages.LeaguePage import LeaguePage
from pages.LoginPage import LoginPage
from pages.WelcomePage import WelcomePage
from pages.components.BottomNav import BottomNav


def before_all(context):
    context.driver = DriverManager.get_driver()
    context.welcome_page = WelcomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.bottom_nav = BottomNav(context.driver)
    context.favorites_page = FavoritesPage(context.driver)
    context.league_page = LeaguePage(context.driver)


def after_all(context):
    context.driver.quit()
