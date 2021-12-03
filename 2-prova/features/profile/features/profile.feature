Feature: Profile;

  Scenario: Successful user name editing;
    Given that the user is logged into the platform and is on the 'Profile' page
    When the user correctly edits the required field 'Full name' and clicks 'Save data'
    Then the Site returns a message confirming to the user that the 'Full Name' field has been changed.
