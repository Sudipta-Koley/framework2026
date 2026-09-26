from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.Base_Page import BasePage
from config.config import URL,HOMEPAGE_URL

class CartPage(BasePage):

    CART_ICON = (By.XPATH,  "//div[@id='shopping_cart_container']")
    QTY = (By.XPATH,  "//div[text()='QTY']")
    DESCRIPTION = (By.XPATH,  "//div[text()='Description']")
    TITLE= (By.XPATH,  "//span[text()='Your Cart']")


    def open(self):
            """ Open the login page."""
            super().open(URL)

    def click_cart(self):
            self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
    def get_qty(self):
            return self.get_text(self.QTY)
    def get_description(self):
            return self.get_text(self.DESCRIPTION)
    def get_header(self):
            return self.get_text(self.TITLE)

    def get_text(self, locator):
            return self.wait.until(EC.visibility_of_element_located(locator)).text.strip()                 
          