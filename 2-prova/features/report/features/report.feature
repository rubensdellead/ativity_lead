Feature: General Report;

  Scenario: Search for a report successfully;
    Given that the user is logged into the site, and is on the 'General Report' screen
    When you select an existing edition
    Then the edit selected by the user is exposed, making the edits for that option visible to the user