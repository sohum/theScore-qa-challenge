from behave import when, then


class LeagueSteps(object):

    @then('the user lands on the "{league_title}" league page')
    def is_user_on_page(context, league_title):
        assert league_title == context.league_page.get_league_title(), "User did not land on the {} league page".format(league_title)

    @when('the user selects the "{tab_name}" tab')
    def go_to_tab(context, tab_name):
        context.league_page.tab(tab_name)

    @then('the user lands on the league "{tab_name}"')
    def is_tab_active(context, tab_name):
        assert context.league_page.is_tab_selected(tab_name), "User did not land on the {} sub-tab".format(tab_name)

    @then('the team "{team_name}" is displayed in the league table')
    def is_team_displayed(context, team_name):
        assert context.league_page.is_team_displayed(team_name), "Data in table does not correspond to the correct league."
