

class LoginSteps(object):

    def __init__(self, welcome_page, login_page):
        self.welcome_page = welcome_page
        self.login_page = login_page

    def login(self, email, password):
        self.welcome_page.login()
        self.login_page.login_with_email(email, password)
