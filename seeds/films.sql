DROP TABLE IF EXISTS films;

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT,
    image_url TEXT
);

TRUNCATE table films;

INSERT INTO films (title, release_year, image_url) VALUES ('Star Wars: Episode V - The Empire Strikes Back', 1980, 'https://m.media-amazon.com/images/I/81tqFszxN5S._AC_UF894,1000_QL80_.jpg');
INSERT INTO films (title, release_year, image_url) VALUES ('The Lord of the Rings: The Fellowship of the Ring', 2001, 'https://i.ebayimg.com/00/s/MTYwMFgxMDcx/z/lfoAAOSwzhRjxaQQ/$_57.JPG?set_id=8800005007');
INSERT INTO films (title, release_year, image_url) VALUES ('Pirates of the Caribbean: Dead Man''s Chest', 2006, 'https://i.ebayimg.com/images/g/RWUAAOSwkNZUlG~3/s-l1200.jpg');
INSERT INTO films (title, release_year, image_url) VALUES ('Avengers: Endgame', 2019, 'https://m.media-amazon.com/images/I/71UCkI9EWhL._AC_UF894,1000_QL80_.jpg');