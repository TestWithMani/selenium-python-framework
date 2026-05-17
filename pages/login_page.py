from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.ID, "flash")

    # Actions
    def open_url(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, usr):
        username_field = self.driver.find_element(*self.username)
        username_field.send_keys(usr)

    def enter_password(self, psw):
        password_field  =self.driver.find_element(*self.password)
        password_field.send_keys(psw)

    def click_login_btn(self):
        login_button = self.driver.find_element(*self.login_btn)
        login_button.click()

    def get_success_message(self):
        message = self.driver.find_element(*self.SUCCESS_MSG)
        print(message.text)
        return message.text







