from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@then('I check if cart badge equals "(.*)"')
def step_impl(context, expected_badge_value):
    cart_badge = context.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_badge.text == expected_badge_value


@step('I click on product "(.*)"')
def step_impl(context, product_name):
    product = context.driver.find_element(By.XPATH, f'//div[text()="{product_name}"]')
    product.click()


@step('I add "(.*)" to cart')
def step_impl(context, product_name):
    product = context.driver.find_element(By.XPATH, f'//div[text()="{product_name}"]')
    product.click()
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[contains(.,'Add to cart')]")
    add_to_cart_button.click()
