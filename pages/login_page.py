import os
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.base_url            = os.getenv("BASE_URL", "https://sheguidesme.com/")
        self.login_button        = page.get_by_role("button", name="Login").first
        self.email_input         = (
            page.locator("form")
                .filter(has_text="Email or Phone")
                .get_by_placeholder("Email or Phone Number")
        )
        self.password_input      = page.get_by_role("textbox", name="************")
        self.submit_login_button = page.get_by_role("button", name="Login").nth(1)

    def open_home(self):
        self.navigate(self.base_url)       # ← uses BasePage.navigate() now

    def login(self, email: str = None, password: str = None):
        email    = email    or os.getenv("TEST_EMAIL")
        password = password or os.getenv("TEST_PASSWORD")

        self.login_button.click()
        self.email_input.click()
        self.email_input.fill(email)
        self.password_input.click()
        self.password_input.fill(password)
        self.submit_login_button.click()