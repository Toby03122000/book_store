from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

"""
route /users/new
fill in form
submit it
check new book is in list of books
"""
def test_form_adds_new_user_to_users_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/users.sql")
    page.goto("http://127.0.0.1:5001/users/new")
    page.get_by_placeholder("Username").fill("Jimmy McGill")
    page.get_by_placeholder("Password").fill("S4ulG00dm4n")
    page.get_by_role("button", name="Submit").click()
    