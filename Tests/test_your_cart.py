import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage,BasePage
from config.config import USERNAME, PASSWORD


@pytest.fixture(scope="class")
def cart_page(class_driver):
    login = LoginPage(class_driver)
    login.open()
    login.login(USERNAME, PASSWORD)
    cart = CartPage(class_driver)
    cart.click_cart()  # clicks cart icon after login — no direct URL
    return cart


class TestCart:
    @pytest.fixture(autouse=True)
    def _setup(self, cart_page):
        self.cart_page = cart_page

    @pytest.mark.smoke
    def test_cart_page_displayed(self):
        """TC-01 | Cart page must show 'Your Cart' title."""
        assert self.cart_page.get_header(), \
            "Cart page did not load."

    

    @pytest.mark.smoke
    def test_cart_qty_column(self):
        """TC-03 | QTY column header must be visible."""
        assert self.cart_page.get_qty() == "QTY"
  
    @pytest.mark.smoke
    def test_cart_description_column(self):
        """TC-04 | Description column header must be visible."""
        assert self.cart_page.get_description() == "Description"