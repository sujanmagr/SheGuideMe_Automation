from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.post_page import PostPage


def test_create_post(page):

    login_page = LoginPage(page)
    home_page  = HomePage(page)
    post_page  = PostPage(page)

    # Step 1 — authenticate (reads credentials from .env)
    login_page.open_home()
    login_page.login()

    # Step 2 — navigate to feed
    home_page.go_to_home_feed()
    home_page.verify_post_box_visible()

    # Step 3 — create a post with an image
    post_page.create_post(
        text="Hello this is my first post"
        # image_path="harley-davidson-eeTJKC_wz34-unsplash.jpg",
    )

    # Step 4 — return to home and verify
    login_page.open_home()
    post_page.verify_post_submitted()
