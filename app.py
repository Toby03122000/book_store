from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from film_repository import FilmRepository
from film import Film

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Toby", "Fay", "Harold",]
    return render_template("team.html", team=team)

@app.route('/quotes', methods=['GET'])
def book_quotes():
    book_quotes = ["“The more that you read, the more things you will know. The more that you learn, the more places you'll go.” — Dr. Seuss",
            "“A reader lives a thousand lives before he dies... The man who never reads lives only one.” — George R.R. Martin",
            "“Books are a uniquely portable magic.” — Stephen King",
            "“Reading gives us someplace to go when we have to stay where we are.” — Mason Cooley",
            "“One child, one teacher, one book, and one pen can change the world.” — Malala Yousafzai"]
    film_quotes = ["“A film is - or should be - more like music than like fiction. It should be a progression of moods and feelings.” — Stanley Kubrick",
            "“Cinema should make you forget you are sitting in a theater.” — Roman Polanski",
            "“Cinema is a matter of what's in the frame and what's out.” — Martin Scorsese",
            "“The cinema is not an art which films life: the cinema is something between art and life.” — Jean-Luc Godard",
            "“A film is a petrified fountain of thought.” — Jean Cocteau"]
    return render_template("quotes.html", book_quotes=book_quotes, film_quotes=film_quotes)

@app.route('/book_list', methods=['GET'])
def get_book_list():
    return [
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

@app.route('/authors', methods=['GET'])
def authors():
    return [
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

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(id=None, title=book_details["title"], author=book_details["author"], image_url=book_details["image_url"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/films', methods=['POST'])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(id=None, title=film_details["title"], release_year=film_details["release_year"], image_url=film_details["image_url"])
    film_repository.create(film)
    return redirect("/films")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)