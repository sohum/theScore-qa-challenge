import pytest
from helpers.DriverManager import DriverManager


class BaseTest(object):

    @pytest.fixture
    def driver(self):
        driver = DriverManager.get_driver()
        yield driver
        driver.quit()
