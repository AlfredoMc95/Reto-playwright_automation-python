from playwright.sync_api import Page, expect

class Signup:
    def __init__(self, page):
        self.page = page
        self.gender1 = page.locator('[for="id_gender1"]')
        self.gender2 = page.locator('[for="id_gender2"]')
        self.password_input = page.locator('//input[@id="password"]')
        self.day_selector = page.locator('[data-qa="days"]')
        self.month_selector = page.locator('[data-qa="months"]')
        self.year_selector = page.locator('[data-qa="years"]')
        self.newsletter_checker = page.locator('//input[@id="newsletter"]')
        self.offers_checker = page.locator('//input[@id="optin"]')
        self.input_first_name = page.get_by_role("textbox", name="First name *")
        self.input_last_name = page.get_by_role("textbox", name="Last name *")
        self.input_company = page.get_by_role("textbox", name="Company", exact=True)
        self.input_address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.input_address2 = page.get_by_role("textbox", name="Address 2")
        self.country_selector = page.get_by_label("Country *")
        self.state_selector = page.get_by_role("textbox", name="State *")
        self.city_selector = page.get_by_role("textbox", name="City * Zipcode *")
        self.zipcode_selector = page.locator("#zipcode")
        self.number_selector = page.get_by_role("textbox", name="Mobile Number *")
        self.create_button = page.get_by_role("button", name="Create Account")

    def select_gender(self, gender: str):
        if(gender =="male"):
            self.gender1.click()
        else:
            self.gender2.click()

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def enter_birth(self, day: int, month: int, year: int):
        self.day_selector.select_option(str(day))
        self.month_selector.select_option(str(month))
        self.year_selector.select_option(str(year))
    
    def select_newsletter(self, newsletter: bool):
        if(newsletter):
            self.newsletter_checker.click()

    def select_offers(self, offers: bool):
        if(offers):
            self.offers_checker.click()

    def fill_user_info(self, name: str, last_name: str, company: str):
        self.input_first_name.fill(name)
        self.input_last_name.fill(last_name)
        self.input_company.fill(company)


    def fill_address_info(self, address: str, address2: str, country: str, state : str, city: str, zipcode: int, number: int ):
        self.input_address.fill(address)
        self.input_address2.fill(address2)
        self.country_selector.select_option(country)
        self.state_selector.fill(state)
        self.city_selector.fill(city)
        self.zipcode_selector.fill(str(zipcode))
        self.number_selector.fill(str(number))

    def click_create_button(self):
        self.create_button.click()

