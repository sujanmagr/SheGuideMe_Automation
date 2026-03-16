from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login(page):

    login_page = LoginPage(page)
    home_page  = HomePage(page)

    login_page.open_home()
    login_page.login()          # reads TEST_EMAIL and TEST_PASSWORD from .env

    home_page.go_to_home_feed()
    home_page.verify_post_box_visible()
