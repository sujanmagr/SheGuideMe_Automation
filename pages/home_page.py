from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.logo_link = page.get_by_role("link", name="sheguidesme")
        self.post_input = page.get_by_role("textbox", name="Post on Advertise-Broadcasting Channel(ABC)/ Only Business Related Content.")

    def go_to_home_feed(self):
        self.logo_link.click()

    def verify_post_box_visible(self):
        expect(self.post_input).to_be_visible()