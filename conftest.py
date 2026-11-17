

import pytest



from utilities.driver_factory import get_driver
from utilities.config_reader import config_read



def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default=None,
        choices=["chrome", "edge"],
        help="Select browser: chrome or edge"
    )
    
    

@pytest.fixture(autouse=True)
def driver(request):

    # Read browser from command line
    browser = request.config.getoption("--browser")

    # If CLI argument is not provided, use config.ini
    if browser is None:
        browser = config_read("browser", "default_browser")

    # Launch selected browser
    driver = get_driver(browser)

    # Provide driver to test case
    yield driver

    # Close browser after test execution
    driver.quit()