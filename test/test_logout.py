from playwright.sync_api import Page
from models.home_page import HomePage
from models.login_page import Login


def test_logout(page: Page):
    homePage = HomePage(page)
    login = Login(page)

    homePage.navegate()
    homePage.click_signup_button()
    login.login_account("asdpedro1@gamil.com", "fredoGodoFredo")
    login.click_login()
    homePage.verifi_text("asd pedro")
    homePage.click_logout_button()