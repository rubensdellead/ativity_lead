Feature: Login;

  Scenario: User login and the platform;
    Given that the user is on the login page
    When they fill in the username and password fields
    Then the system site redirects the user to the home page.