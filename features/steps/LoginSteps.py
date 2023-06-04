from behave import given


class LoginSteps(object):

    @given('the user is logged in')
    def login(context):
        context.welcome_page.login()
        context.login_page.login_with_email()
