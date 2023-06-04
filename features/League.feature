Feature: League page and sub-tab navigation
  Background:
    Given the user is logged in
    Given the user is on the Favorites page

  Scenario: Navigate to a league page
    When the user selects a favorited league
    Then the user lands on the correct league page