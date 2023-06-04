from tests.BaseTest import BaseTest
from pages.LoginPage import LoginPage
from pages.WelcomePage import WelcomePage
from steps.LoginSteps import LoginSteps
import pytest


@pytest.fixture
def login_steps(driver):
    return LoginSteps(WelcomePage(driver), LoginPage(driver))


class TestLogin(BaseTest):
    def test_login(self, login_steps):
        login_steps\
            .login("", "")
