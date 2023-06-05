from behave import given


class LoginSteps(object):

    @given('the user is logged in')
    def login(context):
        if "the user is logged in" not in context.precondition_cache:
            context.welcome_page.login()
            context.login_page.login_with_email()
            context.precondition_cache.add("the user is logged in")
