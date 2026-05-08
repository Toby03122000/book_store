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
    p = page.locator("p")
    expect(p).to_have_text("Here are all of the current books we have in our collection:")

"""
route /books
has list of all books
"""
def test_books_lists_all_books(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("li")
    expected_books = [
        "Book(1, The Gruffalo, Julia Donaldson)",
        "Book(2, Ada Twist, Scientist, Andrea Beaty)",
        "Book(3, The Girl Who Drank the Moon, Kelly Barnhill)",
        "Book(4, Dragons in a Bag, Zetta Elliott)"
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books