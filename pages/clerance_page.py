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


class BmetReg:
    def __init__(self, driver):
        self.driver = driver

        self.select_frst_cntry_of_three = (By.XPATH,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]")
        self.select_second_cntry_of_three = (By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[2]")
        self.select_third_cntry_of_three = (By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[3]")
        self.continue_btn = (By.ID, "com.thane.amiprobashi:id/view")
        self.select_a_skill = (By.ID, "com.thane.amiprobashi:id/tvSkillName")
       # self.gender = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
        self.age = (By.ID, "com.thane.amiprobashi:id/tvSubTitle")
        self.age_value = (By.XPATH,
                          "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[14]")
        self.employer_status = (By.ID, "com.thane.amiprobashi:id/layoutSeeking")
        self.confirmation = (By.ID, "com.thane.amiprobashi:id/layoutWorkYes")
        self.bmet_menu = (By.XPATH,
                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/androidx.appcompat.widget.LinearLayoutCompat[1]/androidx.appcompat.widget.LinearLayoutCompat[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat")

    def click_continue_btn(self):
        self.driver.find_element(*self.continue_btn).click()

    def set_frst_desired_cntry(self):
        self.driver.find_element(*self.select_frst_cntry_of_three).click()

    def set_second_desired_cntry(self):
        self.driver.find_element(*self.select_second_cntry_of_three).click()

    def set_third_desired_cntry(self):
        self.driver.find_element(*self.select_third_cntry_of_three).click()

    def set_a_skill(self):
        self.driver.find_element(*self.select_a_skill).click()

    # def select_gender(self):
    #     self.driver.find_element(*self.gender).click()

    def click_age(self):
        self.driver.find_element(*self.age).click()

    def select_age_value(self):
        self.driver.find_element(*self.age_value).click()

    def set_employer_status(self):
        self.driver.find_element(*self.employer_status).click()

    def select_confirmation(self):
        self.driver.find_element(*self.confirmation).click()

    def click_bmet_menu(self):
        self.driver.find_element(*self.bmet_menu).click()
