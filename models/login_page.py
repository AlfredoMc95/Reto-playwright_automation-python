from playwright.sync_api import Page, expect

class Login:
    def __init__(self, page):
        self.page = page
        self.user_name_input = page.get_by_placeholder("Name")
        self.user_email_input= page.locator('.signup-form').get_by_placeholder("Email Address")
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.email_input = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
    

    def enter_username(self, username: str , useremail: str):
        self.user_name_input.fill(username)
        self.user_email_input.fill(useremail)

    def click_register(self):
        self.signup_button.click()

    def login_account(self, username: str, password: str):
        self.email_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()