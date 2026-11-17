
from selenium import webdriver


GRID_URL = "http://localhost:4444"


def get_driver(browser):

    browser_name = browser.lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    return driver
