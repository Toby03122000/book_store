DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

TRUNCATE table users;

INSERT INTO users (username, password) VALUES ('Toby', '123');
INSERT INTO users (username, password) VALUES ('Fay', 'abc');
INSERT INTO users (username, password) VALUES ('Harold', '!@£');