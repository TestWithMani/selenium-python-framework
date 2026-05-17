from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url()
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login_btn()
    login.get_success_message()

    assert "You logged into a secure area!" in login.get_success_message()
