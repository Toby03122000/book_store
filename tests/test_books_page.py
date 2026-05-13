from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

"""
route /books
has title
"""
def test_books_has_title(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Books")

"""
route /books
has text
"""
def test_books_has_text(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    p1 = page.locator("p1")
    expect(p1).to_have_text("Here are all of the current books we have in our collection!")

"""
route /books
has list of all books
"""
def test_books_lists_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    actual_titles = page.locator(".book-card h3").all_inner_texts()
    expected_titles = [
        "The Hitchhiker's Guide to the Galaxy",
        "The Hunger Games",
        "Sapiens: A Brief History of Humankind",
        "The Satsuma Complex",
    ]
    assert actual_titles == expected_titles

"""
route /books
has list of all authors
"""
def test_books_lists_all_authors(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    author_list = page.locator("#author-list")
    expect(author_list).to_have_text([
        "Author: Douglas Adams",
        "Author: Suzanne Collins",
        "Author: Yuval Noah Harari",
        "Author: Bob Mortimer",
    ])

"""
route /books
fill in form
submit it
check new book is in list of books
"""
def test_form_adds_new_book_to_book_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("A Game of Thrones")
    page.get_by_placeholder("Author").fill("George R. R. Martin")
    page.get_by_placeholder("Image url").fill("https://m.media-amazon.com/images/I/71Jzezm8CBL._AC_UF894,1000_QL80_.jpg")
    page.get_by_role("button", name="Submit").click()
    actual_titles = page.locator(".book-card h3").all_inner_texts()
    expected_titles = [
        "The Hitchhiker's Guide to the Galaxy",
        "The Hunger Games",
        "Sapiens: A Brief History of Humankind",
        "The Satsuma Complex",
        "A Game of Thrones"
    ]
    assert actual_titles == expected_titles
    author_list = page.locator("#author-list")
    expect(author_list).to_have_text([
        "Author: Douglas Adams",
        "Author: Suzanne Collins",
        "Author: Yuval Noah Harari",
        "Author: Bob Mortimer",
        "Author: George R. R. Martin"
    ])