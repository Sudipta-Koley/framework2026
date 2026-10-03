# =============================================================
#  tests/test_login.py
# =============================================================

import pytest
from pages.login_page import LoginPage
from config.config import USERNAME,PASSWORD


@pytest.fixture
def login_page(class_driver):
    """One LoginPage instance for the whole class — browser stays open."""
    return LoginPage(class_driver)


class TestLogin:

    @pytest.fixture(autouse=True)
    def _open_login(self, login_page):
        """Navigates to a fresh login form before every test."""
        self.login_page = login_page
        self.login_page.open()

    # ----------------------------------------------------------

    @pytest.mark.negative
    def test_invalid_password(self):
        """TC-01 | Wrong password must show an error toast."""
        self.login_page.login(USERNAME, "WrongPassword@99")
        assert self.login_page.get_error_message() != "", \
            "No error shown for incorrect password."

    @pytest.mark.negative
    def test_invalid_username(self):
        """TC-02 | Unregistered email must show an error toast."""
        self.login_page.login("notregistered@example.com", PASSWORD)
        assert self.login_page.get_error_message() != "", \
            "No error shown for unregistered email."

    @pytest.mark.negative
    def test_empty_credentials(self):
        """TC-03 | Empty form must not navigate away from login."""
        self.login_page.click_login()
        assert not self.login_page.is_login_successful(), \
            "Login succeeded with empty credentials — unexpected."

    @pytest.mark.negative
    def test_empty_username(self):
        """TC-04 | Password only — must not login without email."""
        self.login_page.enter_password(PASSWORD)
        self.login_page.click_login()
        assert not self.login_page.is_login_successful(), \
            "Login succeeded without an email — unexpected."

    @pytest.mark.negative
    def test_empty_password(self):
        """TC-05 | Email only — must not login without password."""
        self.login_page.enter_username(USERNAME)
        self.login_page.click_login()
        assert not self.login_page.is_login_successful(), \
            "Login succeeded without a password — unexpected."

    @pytest.mark.smoke
    def test_valid_login(self):
        """TC-06 | Valid credentials must redirect to the dashboard."""
        self.login_page.login(USERNAME,PASSWORD)
        assert self.login_page.is_login_successful(), \
            "Login failed: did not reach the dashboard URL."
