from playwright.sync_api import Page, expect

"""
route /books
has title
"""
def test_books_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Books")

"""
route /books
has text
"""
def test_books_has_text(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    p1 = page.locator("p1")
    expect(p1).to_have_text("Below are all of the current books we have in our collection:")

"""
route /books
has list of all books
"""
def test_books_lists_all_books(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    # book_cards = page.locator(".book_card")
    actual_titles = page.locator(".book-card h3").all_inner_texts()
    expected_titles = [
        "The Hitchhiker's Guide to the Galaxy",
        "The Hunger Games",
        "Sapiens: A Brief History of Humankind",
        "The Satsuma Complex"
    ]
    assert actual_titles == expected_titles