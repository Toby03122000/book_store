from playwright.sync_api import Page, expect

"""
test has title
"""
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Hello and welcome to Toby's Terrific Tales!")