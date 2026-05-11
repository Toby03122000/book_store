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
    p1 = page.locator("p1")
    expect(p1).to_have_text("Here are all of the current films we have in our collection!")

"""
route /films
has list of all films
"""
def test_films_lists_all_films(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    # film_cards = page.locator(".film_card")
    actual_titles = page.locator(".film-card h3").all_inner_texts()
    expected_titles = [
        "Star Wars: Episode V - The Empire Strikes Back",
        "The Lord of the Rings: The Fellowship of the Ring",
        "Pirates of the Caribbean: Dead Man's Chest",
        "Avengers: Endgame",
        "Project Hail Mary"
    ]
    assert actual_titles == expected_titles