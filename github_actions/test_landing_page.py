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
from github_actions.utility import Toolbox


@mark.landing_page
class TestLandinPage(Toolbox):

    def test_landing_page(self):
        Toolbox.login_to_app(self)
        self.driver.back()
        # check for text
        check_for_text = Toolbox.wait(self).until(EC.presence_of_element_located((By.XPATH, "//a[.='Zero Bank']"))).text
        assert check_for_text == "Zero Bank"

    def test_logout(self):
        Toolbox.logout(self)

    def test_tear_up(self):
        Toolbox.tear_up(self)