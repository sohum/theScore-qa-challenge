from behave import given, when


class FavoritesSteps(object):

    @given('the user is on the Favorites page')
    def go_to_tab(context):
        context.bottom_nav.favorites()

    @when('the user selects the "{chip_name}" favorited league')
    @given('the user is on the "{chip_name}" league page')
    def select_a_favorite(context, chip_name):
        context.favorites_page.select_chip(chip_name)
