import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests(unittest.TestCase):
    usernameErrorMessage = "Epic sadface: Username is required"
    passwordErrorMessage = "Epic sadface: Password is required"
    invalidCredentialsErrorMessage = "Epic sadface: Username and password do not match any user in this service"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        self.submit = self.driver.find_element(By.ID, "login-button")

    def tearDown(self):
        self.driver.quit()

    def testSpecialCharactersInUsername(self):
        self.username.send_keys("#$%^&*\";")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testSpecialCharactersInPassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("#$%^&*\";")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testSQLInjection(self):
        self.username.send_keys("' OR 1=1 --")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testXSS(self):
        self.username.send_keys("<script>alert('XSS')</script>")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testInvalidLogin(self):
        self.username.send_keys("invalid_user")
        self.password.send_keys("invalid_password")
        self.submit.click()

        self.assertFalse("inventory.html" in self.driver.current_url)

    def testEmptyUsername(self):
        self.username.send_keys("")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.usernameErrorMessage, self.driver.page_source)

    def testEmptyPassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("")
        self.submit.click()

        self.assertIn(self.passwordErrorMessage, self.driver.page_source)

    def testEmptyUsernameAndPassword(self):
        self.username.send_keys("")
        self.password.send_keys("")
        self.submit.click()

        self.assertIn(self.usernameErrorMessage, self.driver.page_source)

    def testUppercaseUsername(self):
        self.username.send_keys("STANDARD_USER")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testUppercasePassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("SECRET_SAUCE")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testUppercaseUsernameAndPassword(self):
        self.username.send_keys("STANDARD_USER")
        self.password.send_keys("SECRET_SAUCE")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testValidLogin(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertTrue("inventory.html" in self.driver.current_url)

    def testBlockedUser(self):
        self.username.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn("Epic sadface: Sorry, this user has been locked out.", self.driver.page_source)

    def testProblemUser(self):
        self.username.send_keys("problem_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertTrue("inventory.html" in self.driver.current_url)

    def testPerformanceGlitchUser(self):
        self.username.send_keys("performance_glitch_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertTrue("inventory.html" in self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
