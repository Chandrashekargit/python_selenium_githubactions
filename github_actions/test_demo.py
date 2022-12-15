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


@mark.login
class Test_login(Toolbox):

    def test_signin_and_login(self):
        Toolbox.login_to_app(self)

    def test_logout(self):
        time.sleep(5)
        self.driver.back()
        Toolbox.logout(self)
        time.sleep(5)

    def test_tear_up(self):
        Toolbox.tear_up(self)
