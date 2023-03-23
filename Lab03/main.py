from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def set_up() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    return driver


def navigate_to_url(driver: webdriver.Chrome, url):
    driver.get(url)


def login(driver: webdriver.Chrome, username, password):
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def add_to_cart(driver: webdriver.Chrome, add_to_cart_button_xpath):
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()


def remove_from_cart(driver: webdriver.Chrome, remove_from_cart_button_xpath):
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()


def logout(driver: webdriver.Chrome):
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()


def is_page_title_correct(expected_title):
    driver = set_up()
    navigate_to_url(driver, "https://www.saucedemo.com/")
    assert driver.title == expected_title


def login_tests(url):
    # Test valid credentials
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "secret_sauce")
        assert driver.title == "Swag Labs"
    except AssertionError:
        logging.error(f"Expected title: Swag Labs, actual title: {driver.title}")
        raise
    finally:
        driver.quit()

    # Test invalid username
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "dfasdgeawt", "secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test invalid password
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "dfasdgeawt")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test locked user
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "locked_out_user", "secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Sorry, this user has been locked out.'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Sorry, this user has been locked out., actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test empty username
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "","secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username is required, actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test empty password
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "standard_user", "")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Password is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Password is required, actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test empty username and password
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver, "", "")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username is required'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username is required, actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test special characters in username
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver,"#$%^&*\";","secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test special characters in password
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver,"standard_user","#$%^&*\";")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test special characters in username and password
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver,"#$%^&*\";","#$%^&*\";")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test SQL injection in username
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver,"' OR 1=1 --","secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()

    # Test XSS in username
    driver = set_up()
    try:
        navigate_to_url(driver, url)
        login(driver,"<script>allert(1)</script>","secret_sauce")
        error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        assert error.text == 'Epic sadface: Username and password do not match any user in this service'
    except AssertionError:
        logging.error(
            f"Expected error message: Epic sadface: Username and password do not match any user in this service, "
            f"actual error message: {error.text}")
        raise
    finally:
        driver.quit()


def add_to_cart_tests(url):
    driver = set_up()
    navigate_to_url(driver, url)
    login(driver, "standard_user", "secret_sauce")

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
    is_page_title_correct("Swag Labs")
    login_tests("https://www.saucedemo.com/")
    add_to_cart_tests("https://www.saucedemo.com/")
