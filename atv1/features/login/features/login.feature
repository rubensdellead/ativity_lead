Feature: Login

  Scenario: Valid login (1a)
    Given the user is in the login page
    When hey fills the username and password fields
    Then the system site redirects the user to the home page, but specifically, to the 'Start Menu'





