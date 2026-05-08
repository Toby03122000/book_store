from playwright.sync_api import Page, expect

"""
route /quotes
has title
"""
def test_quotes_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Quotes")

"""
route /quotes
has text
"""
def test_quotes_has_text(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")
    p = page.locator("p")
    expect(p).to_have_text("Famous quotes on the power of reading:")

"""
route /quotes
has list of all quotes
"""
def test_quotes_lists_all_quotes(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")
    quotes = page.locator("li")
    expected_quotes = [
        "“The more that you read, the more things you will know. The more that you learn, the more places you'll go.” — Dr. Seuss",
        "“A reader lives a thousand lives before he dies... The man who never reads lives only one.” — George R.R. Martin",
        "“Books are a uniquely portable magic.” — Stephen King",
        "“Reading gives us someplace to go when we have to stay where we are.” — Mason Cooley"
    ]
    actual_quotes = quotes.all_inner_texts()
    assert actual_quotes == expected_quotes