from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.Base_Page import BasePage
from config.config import URL,HOMEPAGE_URL

class ProductPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    PRODUCT_PRICE = (By.XPATH, "//div[text()='29.99']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@data-test='inventory-item-desc']")
    PRODUCT_IMAGE = (By.XPATH, "//img[@data-test='item-sauce-labs-backpack-img']")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE = (By.XPATH, "//button[text()='Remove']")

    def open(self) -> None:
        """Open the login page."""
        super().open(URL)

    def click_product(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME)).click()

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def get_product_image(self):
        return self.get_text(self.PRODUCT_IMAGE)

    def get_product_description(self):
        return self.get_text(self.PRODUCT_DESCRIPTION)