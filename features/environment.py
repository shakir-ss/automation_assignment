import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    logging.info("Initializing WebDriver...")
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()
    logging.info("WebDriver initialized successfully.")


def after_all(context):
    logging.info("Quitting WebDriver...")
    context.driver.quit()
