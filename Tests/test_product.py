import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage,BasePage
from pages.product_page import ProductPage
from config.config import (
    USERNAME,
    PASSWORD,
    PRODUCT_NAME,
    PRODUCT_PRICE,
    PRODUCT_DESCRIPTION,
    
    
)


@pytest.fixture
def product_page(class_driver):
    login = LoginPage(class_driver)
    login.open()
    login.login(USERNAME, PASSWORD)
    product=ProductPage(class_driver)
    product.click_product()
    return product
    


class TestProduct:
    @pytest.fixture(autouse=True)
    def _setup(self, product_page):
        self.product_page = product_page
    

    @pytest.mark.smoke
    def test_product_name_column(self):
        """TC-01 | PRODUCT NAME column header must be visible."""
        pro=self.product_page.get_product_name()
        print(pro)
        assert self.product_page.get_product_name() == PRODUCT_NAME
  
    @pytest.mark.smoke
    def test_product_image_column(self):
        """TC-04 | Price column header must be visible."""
        assert self.product_page.get_product_image() == PRODUCT_IMAGE

    @pytest.mark.smoke
    def test_product_description_column(self):
        """TC-04 | Price column header must be visible."""
        assert self.product_page.get_product_description() == PRODUCT_DESCRIPTION
    
    @pytest.mark.smoke
    def test_product_price_column(self):
        """TC-04 | Price column header must be visible."""
        assert self.product_page.get_price() == PRODUCT_PRICE