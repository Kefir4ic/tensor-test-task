import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": fr"{os.getcwd()}",
        "download.prompt_for_download": True,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
