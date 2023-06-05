from behave import given, when, then


class FavoritesSteps(object):

    @given('the user is on the "{tab_name}" tab')
    def go_to_tab(context, tab_name):
        context.bottom_nav.tab(tab_name)

    @when('the user selects the "{chip_name}" favorited league')
    @given('the user is on the "{chip_name}" league page')
    def select_a_favorite(context, chip_name):
        context.favorites_page.select_chip(chip_name)

    @then('the user is taken back to the Favorites tab')
    def is_tab_page_displayed(context):
        assert context.favorites_page.is_page_displayed(), 'User was not returned to the Favorites page'
