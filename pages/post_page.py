import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PostPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.post_textbox   = page.locator("textarea")
        self.post_button    = page.get_by_role("button", name="Post")
        self.later_button   = page.get_by_role("button", name="Later")
        self.add_photo_icon = (
            page.locator("div")
                .filter(has_text=re.compile(r"^Add to Your Post$"))
                .locator("path")
                .first
        )

    def click_post_box(self):
        self.page.get_by_role("textbox", name="Post on Advertise-Broadcasting Channel(ABC)/ Only Business Related Content.").click()
        self.post_textbox.click()

    def fill_post_text(self, text: str):
        self.post_textbox.fill(text)

    def dismiss_notification_prompt(self):
        self.later_button.click()

    # def attach_image(self, image_path: str):
    #     self.add_photo_icon.click()
    #     self.page.locator("body").set_input_files(image_path)

    def dismiss_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    def submit_post(self):
        self.post_button.click()

    def create_post(self, text: str):
    # def create_post(self, text: str, image_path: str = None):
        self.click_post_box()
        self.fill_post_text(text)
        self.dismiss_notification_prompt()

        # if image_path:
        #     self.attach_image(image_path)
        #     self.dismiss_dialog()

        self.submit_post()

    def verify_post_submitted(self):
        expect(self.post_textbox).not_to_be_visible()
