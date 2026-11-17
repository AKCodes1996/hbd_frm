
import pytest 






def test_browser_launch(driver):
        driver.get("https://tutorialsninja.com/demo/")
        print("Browser:", driver.capabilities["browserName"])
        assert "Your Store" in driver.title