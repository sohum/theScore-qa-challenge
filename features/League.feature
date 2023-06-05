Feature: League page and sub-tab navigation
  Background:
    Given the user is logged in
    Given the user is on the Favorites page

  Scenario: Navigate to a league page
    When the user selects the "ENG" favorited league
    Then the user lands on the "England Soccer" league page

  Scenario: Navigate to a sub-tab
    Given the user is on the "ENG" league page
    When the user selects the "Table" tab
    Then the user lands on the league "Table"
    And the team "Manchester City" is displayed in the league table
