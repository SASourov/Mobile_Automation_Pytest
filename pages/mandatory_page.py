from selenium.webdriver.common.by import By


class MandatoryPage:
    def __init__(self, driver):
        self.driver = driver

        self.bmet_reg_menu = (By.ID, "com.thane.amiprobashi:id/dialogTextEmail2")
        self.continue_btn = (By.ID, "com.thane.amiprobashi:id/view")
        self.password = (By.ID, "com.thane.amiprobashi:id/et_password")

    def set_user(self, user):
        self.driver.find_element(*self.bmet_reg_menu).send_keys(user)

    def click_continue_btn(self):
        self.driver.find_element(*self.continue_btn).click()

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.continue_btn).click()