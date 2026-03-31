from playwright.sync_api import Page
from models.home_page import HomePage
from models.login_page import Login
from models.signup_page import Signup
from models.account_created_page import Create_account
from models.account_deleted_page import Delete_account

def test_register(page: Page):
    homePage = HomePage(page)
    login = Login(page)
    signup = Signup(page)
    create_account = Create_account(page)
    delete_account = Delete_account(page)

    homePage.navegate()
    homePage.click_signup_button()
    login.create_user("asd pedro", "asdpedro@gamil.com")
    login.click_register()
    signup.select_gender("male")
    signup.enter_password("fredoGodoFredo")
    signup.enter_birth(2,10,1995)
    signup.select_newsletter(True)
    signup.select_offers(True)
    signup.fill_user_info("name test","lastname test","compannnnn")
    signup.fill_address_info("cr 45 - 123", "cr 55 - 563","Canada","algun estado","alguna ciudad",111111,12365478)
    signup.click_create_button()
    create_account.verifi_text()
    create_account.continue_click()
    homePage.verifi_text("asd pedro")
    homePage.click_delete_button()
    delete_account.verifi_text()
    delete_account.continue_click()