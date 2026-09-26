# =============================================================
#  pages/login_page.py
#
#  BEGINNER GUIDE — How this file works:
#
#  1. LOCATORS  — CSS/XPath selectors that find elements on the page
#  2. ACTIONS   — Methods that interact with those elements
#  3. STATE     — Methods that read the result (used by tests to assert)
#
#  Rule: NO assert statements here. Tests do the asserting.
#        This file only performs actions and returns values.
#
#  App flow:
#    Landing page loads → click "Log in" → form appears
#    → fill email + password → click "Login" → dashboard
# =============================================================

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.Base_Page import BasePage
from config.config import URL,HOMEPAGE_URL

class LoginPage(BasePage):

    # ----------------------------------------------------------
    #  LOCATORS
    #  Format: (By.STRATEGY, "value")
    #  These are the only things that change when the UI changes.
    # ----------------------------------------------------------

        
    USERNAME = (By.ID,    'user-name')
    PASSWORD = (By.ID,    'password')
    LOGINBTN = (By.ID,     'login-button')
    ERRMSG   = (By.XPATH,  "//h3[text()='Epic sadface: Username and password do not match any user in this service']")

    # ----------------------------------------------------------
    #  NAVIGATION
    # ----------------------------------------------------------

    
    # ----------------------------------------------------------
    #  ACTIONS
    # ----------------------------------------------------------
    
    def open(self):
        """ Open the login page."""
        super().open(URL)

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGINBTN)).click()

    def login(self, username, password):
        """Shortcut: fills both fields and clicks Login in one call."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ----------------------------------------------------------
    #  STATE READS  (return values — never assert here)
    # ----------------------------------------------------------

    def get_error_message(self):
        """Returns the error toast text. Returns '' if no toast appears."""
        try:
            el = self.wait.until(
                EC.visibility_of_element_located(self.ERRMSG)
            )
            return el.text.strip()
        except TimeoutException:
            return ""

    def is_login_successful(self):
        """Returns True when the browser reaches the dashboard page."""
        try:
            self.wait.until(EC.url_to_be(HOMEPAGE_URL))
            return True
        except TimeoutException:
            return False
