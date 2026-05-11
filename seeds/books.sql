DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    image_url TEXT
);

INSERT INTO books (title, author, image_url) VALUES ('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 'https://cdn.waterstones.com/bookjackets/large/9781/5290/9781529034523.jpg');
INSERT INTO books (title, author, image_url) VALUES ('The Hunger Games', 'Suzanne Collins', 'https://primarybooks.co.uk/cdn/shop/products/9781407153339_grande.jpg?v=1589805683');
INSERT INTO books (title, author, image_url) VALUES ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'https://m.media-amazon.com/images/I/713jIoMO3UL.jpg');
INSERT INTO books (title, author, image_url) VALUES ('The Satsuma Complex', 'Bob Mortimer', 'https://m.media-amazon.com/images/I/61+TO1FmPJL.jpg');