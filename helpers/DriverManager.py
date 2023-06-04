import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


class DriverManager(object):

    @staticmethod
    def get_driver(custom_opts=None):
        absolute_path = os.path.dirname(__file__)
        app_relative_path = '../thescore_23.6.0.apk'
        app_full_path = os.path.join(absolute_path, app_relative_path)

        caps = {
            'platformName': 'Android',
            'appium:deviceName': 'Android',
            'appium:app': app_full_path,
            'appium:automationName': 'uiautomator2',
            'appium:autoGrantPermissions': True
        }

        options = UiAutomator2Options().load_capabilities(caps)
        if custom_opts is not None:
            options.load_capabilities(custom_opts)
        return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)
