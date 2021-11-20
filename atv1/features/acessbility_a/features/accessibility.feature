Feature: Accessibility menu
  Scenario - User to increase the site's font (4a)
    Given that the user is logged into the site, and is on any screen of the site and the increase font function is available (4a)
    When they click on 'Increase Font
    Then the font of the whole site is changed according to the clicks on the button the user is on

Feature: Accessibility menu
  Scenario - User to change the page contrast (4b)
    Given the user is logged into the platform and is in any function of the site (4b)
    When they clicks on the 'Toggle high-contrast' function of the site
    Then the site returns only two colors, black and yellow, to the user
