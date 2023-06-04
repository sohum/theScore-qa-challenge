from behave import then


class LeagueSteps(object):

    @then('the user lands on the "{league_title}" league page')
    def is_user_on_page(context, league_title):
        assert league_title == context.league_page.get_league_title(), 'User did not land on the correct league page'
