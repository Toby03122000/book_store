from playwright.sync_api import Page, expect

"""
test has title
"""
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Toby's Terrific Tales (TTT)")

"""
test has welcome message
"""
def test_has_welcome_message(page: Page):
    page.goto("http://127.0.0.1:5001")
    welcome_message = page.locator("#welcome-message")
    expect(welcome_message).to_have_text("Hey everone and welcome to TTT!")

"""
test book features list has content
"""
def test_book_features_list(page: Page):
    page.goto("http://127.0.0.1:5001")
    list_items = page.locator("#book-features li")
    expect(list_items).to_have_text([
        "Cover (well, one of)",
        "Title",
        "Author's name"
    ])

"""
test film features list has content
"""
def test_film_features_list(page: Page):
    page.goto("http://127.0.0.1:5001")
    list_items = page.locator("#film-features li")
    expect(list_items).to_have_text([
        "Original cinema poster",
        "Title",
        "Release date"
    ])

"""
test has closing message
"""
def test_has_closing_message(page: Page):
    page.goto("http://127.0.0.1:5001")
    closing_message = page.locator("#closing-message")
    expect(closing_message).to_have_text("Now, go forth and find your next captivating enthrallment...")