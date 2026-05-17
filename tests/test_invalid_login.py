from pages.login_page import LoginPage

def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url()
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login_btn()
    text_msg = login.get_success_message()

    assert "This is invalid Login" not in text_msg