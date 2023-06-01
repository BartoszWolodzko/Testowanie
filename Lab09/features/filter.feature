Feature: Check filter products functionality

  Scenario: Filter by Name (A to Z)
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I filter by "Name (A to Z)"
    Then I check if the first product is "Sauce Labs Backpack"

  Scenario: Filter by Name (Z to A)
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I filter by "Name (Z to A)"
    Then I check if the first product is "Test.allTheThings() T-Shirt (Red)"

  Scenario: Filter by Price (low to high)
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I filter by "Price (low to high)"
    Then I check if the first product is "Sauce Labs Onesie"

  Scenario: Filter by Price (high to low)
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I filter by "Price (high to low)"
    Then I check if the first product is "Sauce Labs Fleece Jacket"