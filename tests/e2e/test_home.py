import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://localhost:5001")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("uv-fasthtml"))

def test_go_to_login_page(page: Page):
    page.goto("http://localhost:5001")

    # Click the get started link.
    page.get_by_role("link", name="Login").click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("uv-fasthtml"))
