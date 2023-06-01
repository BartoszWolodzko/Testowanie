Feature: Check cart functionality

  Scenario: Add to cart and check cart badge on the same site
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I add "Sauce Labs Backpack" to cart
    And I go to previous page
    And I add "Sauce Labs Bike Light" to cart
    Then I check if cart badge equals "2"

  Scenario: Add to cart and check cart badge after refresh
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I add "Sauce Labs Backpack" to cart
    And I go to previous page
    And I add "Sauce Labs Bike Light" to cart
    When I refresh the page
    Then I check if cart badge equals "2"

  Scenario: Add to cart and check cart badge on different sites
    Given I am on the Sauce Demo login page
    When I enter valid username
    When I enter valid password
    And I click the login button
    Then I should be logged in successfully
    And I add "Sauce Labs Backpack" to cart
    And I go to previous page
    And I add "Sauce Labs Bike Light" to cart
    And I go to previous page
    Then I check if cart badge equals "2"
    And I click on product "Sauce Labs Backpack"
    Then I check if cart badge equals "2"
    And I go to previous page
    Then I check if cart badge equals "2"
    And I click on product "Sauce Labs Bike Light"
    Then I check if cart badge equals "2"