from selenium.webdriver.common.by import By


class OpenApp:
    def __init__(self, driver):
        self.driver = driver

        self.allow_btn = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.language = (By.ID, "com.thane.amiprobashi:id/tvLanguageEn")
        self.nxt_btn = (By.ID, "com.thane.amiprobashi:id/tvButtonText")

    def click_allow_btn(self):
        self.driver.find_element(*self.allow_btn).click()

    def select_language(self):
        self.driver.find_element(*self.language).click()

    def click_nxt_btn(self):
        self.driver.find_element(*self.nxt_btn).click()





