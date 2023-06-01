from behave import *

use_step_matcher("re")


@when("I refresh the page")
def step_impl(context):
    context.driver.refresh()


@step("I go to previous page")
def step_impl(context):
    context.driver.back()