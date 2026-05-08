from film import Film

class FilmRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["id"], row["title"], row["release_year"])
            films.append(item)
        return films

    # Find a single film by their id
    # def find(self, film_id):
    #     rows = self._connection.execute(
    #         'SELECT * from films WHERE id = %s', [film_id])
    #     row = rows[0]
    #     return Film(row["id"], row["title"], row["director"])

    # Create a new film
    # Do you want to get its id back? Look into RETURNING id;
    # def create(self, film):
    #     self._connection.execute('INSERT INTO films (title, director) VALUES (%s, %s)', [
    #                             film.title, film.director])
    #     return None

    # Delete an film by their id
    # def delete(self, film_id):
    #     self._connection.execute(
    #         'DELETE FROM films WHERE id = %s', [film_id])
    #     return None