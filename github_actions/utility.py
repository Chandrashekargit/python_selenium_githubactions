from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from pytest import mark
from dotenv import load_dotenv
import os


class Toolbox:
    load_dotenv()

    def wait(self):
        wait = WebDriverWait(self.driver, 20, poll_frequency=3)
        return wait

    def login_to_app(self):

        # signin link
        signin_btn = self.wait().until(EC.presence_of_element_located((By.XPATH, "//button[@id='signin_button']")))
        signin_btn.click()

        # login screen
        un = self.wait().until(EC.presence_of_element_located((By.XPATH, "//input[@id='user_login']")))
        un.send_keys(os.getenv('UNAME'))
        pw = self.wait().until(EC.presence_of_element_located((By.XPATH, "//input[@id='user_password']")))
        pw.send_keys(os.getenv('PASSWD'))
        submit_btn = self.wait().until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        submit_btn.click()

    def logout(self):
        # logout
        access_logout_option = self.wait().until(EC.presence_of_element_located((By.XPATH, "//li[3]//a[@class='dropdown-toggle']")))
        access_logout_option.click()

        logout = self.wait().until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_link']")))
        logout.click()

    def tear_up(self):
        self.driver.quit()