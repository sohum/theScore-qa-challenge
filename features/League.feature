Feature: League page and sub-tab navigation
  Background:
    Given the user is logged in
    Given the user is on the "Favorites" tab

  Scenario Outline: Navigate to a league page
    When the user selects the "<chip_name>" favorited league
    Then the user lands on the "<league_name>" league page

    Examples: Soccer leagues
      | chip_name | league_name    |
      | ENG       | England Soccer |
      | ESP       | Spain Soccer   |
      | GER       | Germany Soccer |

  Scenario Outline: Navigate to a league table
    Given the user is on the "<chip_name>" league page
    When the user selects the "Table" tab
    Then the user lands on the league "Table"
    And the team "<team_name>" is displayed in the league table

    Examples: Soccer leagues
      | chip_name | team_name       |
      | ENG       | Manchester City |
      | ESP       | Barcelona       |
      | GER       | Bayern Munich   |

  Scenario Outline: Navigate back from a league table
    Given the user is on the "<chip_name>" league "Table"
    When the user navigates back
    Then the user is taken back to the Favorites tab

    Examples: Soccer leagues
      | chip_name |
      | ENG       |
      | ESP       |
      | GER       |