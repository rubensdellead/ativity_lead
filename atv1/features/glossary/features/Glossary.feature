Feature: Glossary

  Scenario: Search for a term in the glossary (2a)
    Given that the user is logged into the site, and is on the 'Glossary' screen;
    When they type in an existing term
    Then the corresponding search terms are listed for the user