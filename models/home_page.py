from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_buttton = page.get_by_text(" Signup / Login")
        self.user_text = page.get_by_text(" Delete Account")
        self.delete_buttton = page.get_by_text(" Delete Account")


    def navegate(self):
        self.page.goto("https://automationexercise.com/")

    def click_signup_button(self):
        self.login_buttton.click()

    def verifi_text(self, username: str):
        expect(self.page.get_by_text(f"Logged in as {username}")).to_be_visible()

    def click_delete_button(self):
        self.delete_buttton.click()