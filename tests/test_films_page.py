from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

"""
route /films
has title "Films"
"""
def test_has_title(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Films")

"""
route /films
has text
"""
def test_films_has_text(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    p1 = page.locator("p1")
    expect(p1).to_have_text("Here are all of the current films we have in our collection!")

"""
route /films
has list of all films
"""
def test_films_lists_all_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    actual_titles = page.locator(".film-card h3").all_inner_texts()
    expected_titles = [
        "Star Wars: Episode V - The Empire Strikes Back",
        "The Lord of the Rings: The Fellowship of the Ring",
        "Pirates of the Caribbean: Dead Man's Chest",
        "Avengers: Endgame"
    ]
    assert actual_titles == expected_titles

"""
route /films
has list of all release years
"""
def test_films_lists_all_release_years(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    release_year_list = page.locator("#release-year-list")
    expect(release_year_list).to_have_text([
        "Released: 1980",
        "Released: 2001",
        "Released: 2006",
        "Released: 2019"
    ])

"""
route /films
fill in form
submit it
check new book is in list of films
"""
def test_form_adds_new_film_to_film_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_placeholder("Title").fill("Project Hail Mary")
    page.get_by_placeholder("Release Year").fill("2026")
    page.get_by_placeholder("Image url").fill("https://m.media-amazon.com/images/M/MV5BNTkwNzJiYTctNzI3NC00NjE1LTlhYjktY2Q5MTdmMWFmNzcxXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
    page.get_by_role("button", name="Submit").click()
    actual_titles = page.locator(".film-card h3").all_inner_texts()
    expected_titles = [
        "Star Wars: Episode V - The Empire Strikes Back",
        "The Lord of the Rings: The Fellowship of the Ring",
        "Pirates of the Caribbean: Dead Man's Chest",
        "Avengers: Endgame",
        "Project Hail Mary"
    ]
    assert actual_titles == expected_titles
    release_year_list = page.locator("#release-year-list")
    expect(release_year_list).to_have_text([
        "Released: 1980",
        "Released: 2001",
        "Released: 2006",
        "Released: 2019",
        "Released: 2026"
    ])