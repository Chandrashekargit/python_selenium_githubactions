import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from pytest import mark
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True, scope='class')
def setup(request):
    load_dotenv()
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(os.getenv('BASE_URL'))
    driver.maximize_window()
    request.cls.driver = driver