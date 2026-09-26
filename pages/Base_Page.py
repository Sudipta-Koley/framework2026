# =============================================================
#  pages/base_page.py
#
#  BEGINNER GUIDE — What is BasePage?
#
#  BasePage is the PARENT class that every page object inherits.
#  It holds browser utilities that ALL pages need.
#
#  Withouge has find() →       LoginPage inherits it
#    ProfilePage has find()  →        DashboardPage inherits it
#    (repeated 3 times)               (written once)
#
#  Inheritance syntax:
#    class LoginPage(BasePage):  ← LoginPage gets everything below
# =============================================================

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from config.config import EXPLICIT_WAIT,IMPLICIT_WAIT,USERNAME,PASSWORD


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(60)   # wait up to 60s for page load
        self.driver.set_script_timeout(30)       # wait up to 30s for JS execution
        # WebDriverWait: smarter than time.sleep() — waits only as long as needed
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self, url):
        """Navigate the browser to a URL."""
        try:
            self.driver.get(url)
        except WebDriverException:
            # If page load times out, the DOM may still be usable — continue
            pass

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text.strip()
    def is_element_visible(self, locator):
        """Return True if the element is visible on the page."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def url_contains(self, keyword):
        """Return True if the current URL contains the given keyword."""
        try:
            self.wait.until(EC.url_contains(keyword))
            return True
        except TimeoutException:
            return False

