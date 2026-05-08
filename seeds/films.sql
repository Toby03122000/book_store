DROP TABLE IF EXISTS films;

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT
);

INSERT INTO films (title, release_year) VALUES ('Spider-Man', 2002);
INSERT INTO films (title, release_year) VALUES ('Project Hail Mary', 2026);
INSERT INTO films (title, release_year) VALUES ('Hot Fuzz', 2007);
INSERT INTO films (title, release_year) VALUES ('Ex Machina', 2014);