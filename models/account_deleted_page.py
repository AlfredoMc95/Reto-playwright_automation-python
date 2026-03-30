import re
from playwright.sync_api import expect, Page

class Delete_account:
    def __init__(self, page):
        self.page = page
        self.continue_button = page.get_by_role("link", name="Continue")

    def verifi_text(self):
        expect(self.page.get_by_text("Account Deleted!")).to_be_visible()

    def continue_click(self):
        self.continue_button.click()