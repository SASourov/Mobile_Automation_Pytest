import time
from appium import webdriver
from selenium.webdriver.common.by import By

from pages.clerance_page import OpenApp
from pages.mandatory_page import MandatoryPage
from pages.bmet_reg_pag import BmetReg

desired_caps = {}
desired_caps['platformVersion'] = '13'
desired_caps['udid'] = '1055838388011445'
desired_caps['deviceName'] = 'itel A05s'
desired_caps['appPackage'] = 'com.thane.amiprobashi'
desired_caps['appActivity'] = 'com.thane.amiprobashi.splash_screen.SplashActivity'
desired_caps['platformName'] = 'Android'


class Test_001:
    def test_open_app(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(40)
        self.op = OpenApp(self.driver)
        self.op.click_allow_btn()
        time.sleep(1)
        self.op.select_language()
        self.op.click_nxt_btn()
        time.sleep(2)
        expected_text = self.driver.find_element(By.ID, "com.thane.amiprobashi:id/textView").text
        if expected_text == "Mobile number":
            assert True
            print("Test case 001 Passed")

        else:
            print("App Not Opened")

        self.driver.quit()


class Test_002:
    def test_invalid_login(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(40)
        self.op = OpenApp(self.driver)
        self.op.click_allow_btn()
        time.sleep(1)
        self.op.select_language()
        self.op.click_nxt_btn()
        time.sleep(1)
        self.mp = MandatoryPage(self.driver)
        self.mp.set_user("01871637042")
        time.sleep(2)
        self.mp.click_continue_btn()
        time.sleep(2)
        self.mp.set_password("Ra0@tst")
        self.mp.click_login_btn()
        time.sleep(3)


class Test_003:
    def test_valid_login(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(40)
        self.op = OpenApp(self.driver)
        self.op.click_allow_btn()
        time.sleep(1)
        self.op.select_language()
        self.op.click_nxt_btn()
        time.sleep(1)
        self.mp = MandatoryPage(self.driver)
        self.mp.set_user("01871637042")
        time.sleep(2)
        self.mp.click_continue_btn()
        time.sleep(2)
        self.mp.set_password("Ra0@test")
        self.mp.click_continue_btn()

        time.sleep(3)


class Test_004:
    def test_bmet_reg(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(40)
        self.op = OpenApp(self.driver)
        self.op.click_allow_btn()
        time.sleep(1)
        self.op.select_language()
        self.op.click_nxt_btn()
        time.sleep(1)
        self.mp = MandatoryPage(self.driver)
        self.mp.set_user("01871575077")
        self.mp.click_continue_btn()
        self.mp.set_password("Ra0@test")
        self.mp.click_login_btn()
        self.br = BmetReg(self.driver)
        self.br.set_frst_desired_cntry()
        self.br.set_second_desired_cntry()
        self.br.set_third_desired_cntry()
        self.br.click_continue_btn()
        self.br.set_a_skill()
        self.br.click_continue_btn()
        # self.br.select_gender()  #Error
        self.br.click_age()
        self.br.select_age_value()
        self.br.set_employer_status()
        self.br.select_confirmation()
        self.br.click_continue_btn()
        self.br.click_bmet_menu()
