from playwright.sync_api import Page
from models.home_page import HomePage
from models.login_page import Login

def test_incorrect_login(page: Page):
    homePage = HomePage(page)
    login = Login(page)

    homePage.navegate()
    homePage.click_signup_button()
    login.login_account("asdpedro1@gamil.com", "fakeFredo")
    login.click_login()
    login.verifi_incorrect_user_text()