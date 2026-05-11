from book import Book

class BookRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author"], row["image_url"])
            books.append(item)
        return books

    # Find a single book by their id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author"])

    # Create a new book
    # Do you want to get its id back? Look into RETURNING id;
    # def create(self, book):
    #     self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', [
    #                             book.title, book.author])
    #     return None

    # Delete an book by their id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None