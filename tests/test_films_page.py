from playwright.sync_api import Page, expect

"""
test /films
has title "Films"
"""
def test_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Films")

"""
route /films
has text
"""
def test_films_has_text(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    p = page.locator("p")
    expect(p).to_have_text("Here are all of the current films we have in our collection:")

"""
route /films
has list of all films
"""
def test_films_lists_all_films(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    films = page.locator("li")
    expected_films = [
        "Film(1, Spider-Man, 2002)",
        "Film(2, Project Hail Mary, 2026)",
        "Film(3, Hot Fuzz, 2007)",
        "Film(4, Ex Machina, 2014)",
    ]
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films