from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@then('I check if the first product is "(.*)"')
def step_impl(context, product_name):
    product_label = context.driver.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert product_label.text == product_name


@step('I filter by "(.*)"')
def step_impl(context, filter_option):
    filter_dropdown = context.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_dropdown.click()
    filter_option = context.driver.find_element(By.XPATH, f'//option[text()="{filter_option}"]')
    filter_option.click()
