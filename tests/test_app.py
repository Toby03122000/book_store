import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

"""
GET /books.status_code
returns 200
"""
def test_get_books_returns_200():
    client = app.test_client()
    response = client.get("/book_list")
    assert response.status_code == 200

"""
GET /books.json
returns all books
"""
def test_get_books_returns_all_books():

    client = app.test_client()
    response = client.get("/book_list")

    assert response.json == [
        {
        "title": "The Gruffalo",
        "author": "Julia Donaldson"
        },
        {
        "title": "Ada Twist, Scientist",
        "author": "Andrea Beaty"
        },
        {
        "title": "The Girl Who Drank the Moon",
        "author": "Kelly Barnhill"
        },
        {
        "title": "Dragons in a Bag",
        "author": "Zetta Elliott"
        }
    ]

"""
GET /authors.status_code
returns 200
"""
def test_get_authors_returns_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

"""
GET /authors.json
returns all authors
"""
def test_get_authors_returns_all_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
    {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
]