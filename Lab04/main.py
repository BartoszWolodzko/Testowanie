from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def set_up(some_kind_of_driver):
    driver = some_kind_of_driver
    return driver


def navigate_to_url(driver, url):
    print(f"Opening {url}...")
    sleep(1)
    driver.get(url=url)


def login(driver, username, password, fields):
    username_field = driver.find_element(fields["username"]["by"], fields["username"]["value"])
    password_field = driver.find_element(fields["password"]["by"], fields["password"]["value"])
    login_button = driver.find_element(fields["login_button"]["by"], fields["login_button"]["value"])
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def add_to_cart(driver: webdriver.Chrome, add_to_cart_button_xpath):
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()


def remove_from_cart(driver: webdriver.Chrome, remove_from_cart_button_xpath):
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()


def logout(driver, fields):
    logout_button = driver.find_element(fields["logout_button"]["by"], fields["logout_button"]["value"]).click()


def is_page_title_correct(expected_title, some_kind_of_webdriver):
    driver = set_up(some_kind_of_webdriver)
    navigate_to_url(driver, "https://www.saucedemo.com/")
    assert driver.title == expected_title


def login_tests(url, some_kind_of_webdriver, fields):
    # Test valid credentials
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "secret_sauce", fields)
        assert driver.title == "Swag Labs"
    except AssertionError:
        logging.error(f"Expected title: Swag Labs, actual title: {driver.title}")
        raise
    finally:
        print("Closing browser...")

    # Test invalid username
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "dfasdgeawt", "secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test invalid password
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "dfasdgeawt", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test locked user
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "locked_out_user", "secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Sorry, this user has been locked out.'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Sorry, this user has been locked out., actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test empty username
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "","secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username is required, actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test empty password
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Password is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Password is required, actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test empty username and password
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver, "", "", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username is required, actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test special characters in username
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver,"#$%^&*\";","secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test special characters in password
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver,"standard_user","#$%^&*\";", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test special characters in username and password
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver,"#$%^&*\";","#$%^&*\";", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test SQL injection in username
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver,"' OR 1=1 --","secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")

    # Test XSS in username
    driver = set_up(some_kind_of_webdriver)
    try:
        navigate_to_url(driver, url)
        login(driver,"<script>allert(1)</script>","secret_sauce", fields)
        error = driver.find_element(fields["error"]["by"], fields["error"]["value"])
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        print("Closing browser...")


def add_to_cart_tests(url, some_kind_of_webdriver):
    driver = set_up(some_kind_of_webdriver)
    navigate_to_url(driver, url)
    login(driver, "standard_user", "secret_sauce", fields)

    try:
        # remove_from_cart(driver, "//button[@id='remove-sauce-labs-backpack']")
        add_to_cart(driver, "//button[@id='add-to-cart-sauce-labs-backpack']")
        items_in_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        assert items_in_cart.text == "1"
    except AssertionError:
        logging.error(f"Expected items in cart: 1, actual items in cart: {items_in_cart.text}")
        raise
    except Exception:
        logging.error("Something went wrong")
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    fields = {
        "username": {
            "by": By.XPATH,
            "value": "//input[@id='user-name']",
        },
        "password": {
            "by": By.XPATH,
            "value": "//input[@id='password']",
        },
        "login_button": {
            "by": By.XPATH,
            "value": "//input[@id='login-button']",
        },
        "error": {
            "by": By.XPATH,
            "value": "//h3[@data-test='error']",
        },
        "add_to_cart": {
            "by": By.XPATH,
            "value": "//button[@id='add-to-cart-sauce-labs-backpack']",
        },
        "remove_from_cart": {
            "by": By.XPATH,
            "value": "//button[@id='remove-sauce-labs-backpack']",
        },
        "items_in_cart": {
            "by": By.CSS_SELECTOR,
            "value": ".shopping_cart_badge",
        }
    }
    is_page_title_correct("Swag Labs", webdriver.Chrome())
    login_tests("https://www.saucedemo.com/", webdriver.Chrome(), fields)
    add_to_cart_tests("https://www.saucedemo.com/", webdriver.Chrome())
