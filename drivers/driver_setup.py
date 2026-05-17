from selenium import webdriver

def get_driver(headless=False):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

