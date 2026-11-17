




from selenium import webdriver



def get_driver(browser):
  
  
  browser_name = browser.lower()
  
  if browser_name == "chrome":
    driver = webdriver.Chrome()
  
  elif browser_name == "edge":
    driver =  webdriver.Edge()
  else:
    raise ValueError(f"Unsuported browser: {browser_name}")
  
  
  return driver
  