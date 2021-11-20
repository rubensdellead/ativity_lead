Feature: My courses

  Scenario: Access to lessons for a course (3a)
    Given that the user is logged into the site and is on the 'My Courses' screen
    When the user clicks on 'Enter the Class'
    Then all the content corresponding to that lesson is presented, including videos and exercises