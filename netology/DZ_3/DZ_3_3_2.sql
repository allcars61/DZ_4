INSERT INTO genres (name) VALUES
('rock'),
('pop'),
('hip-hop'),
('electronic'),
('jazz');

INSERT INTO artists (name, genre_id) VALUES
('Queen', 1),
('The Beatles', 1),
('Michael Jackson', 2),
('Eminem', 3),
('Daft Punk', 4),
('Chet Baker', 5),
('Radiohead', 1),
('Beyonce', 2);

INSERT INTO albums (title, year, artist_id) VALUES
('A Night at the Opera', 1975, 1),
('Abbey Road', 1969, 2),
('Thriller', 1982, 3),
('The Slim Shady LP', 1999, 4),
('Discovery', 2001, 5),
('Chet Baker Sings', 1954, 6),
('OK Computer', 1997, 7),
('Lemonade', 2016, 8);

INSERT INTO tracks (title, duration, album_id) VALUES
('Bohemian Rhapsody', 354, 1),
('Come Together', 259, 2),
('Thriller', 358, 3),
('My Name Is', 276, 4),
('One More Time', 320, 5),
('My Funny Valentine', 283, 6),
('Paranoid Android', 386, 7),
('Sorry', 273, 8),
('Get Lucky', 368, 5),
('Space Oddity', 315, 2),
('Don''t Stop ''Til You Get Enough', 354, 3),
('Lose Yourself', 326, 4),
('Digital Love', 292, 5),
('Blackbird', 177, 2),
('Karma Police', 265, 7);

INSERT INTO collections (title, year) VALUES
('Best of Queen', 2020),
('The Beatles Anthology', 1995),
('King of Pop', 2008),
('6 Feet Underground', 2019),
('Daft Club', 2003),
('Chet Baker''s Best', 2010),
('Radiohead: The Best Of', 2008),
('Homecoming: The Live Album', 2019);

INSERT INTO collection_tracks (collection_id, track_id) VALUES
(1, 1),
(1, 7),
(1, 14),
(2, 2),
(2, 5),
(2, 15),
(3, 3),
(3, 11),
(3, 13),
(4, 4),
(4, 8),
(4, 12),
(5, 5),
(5, 9),
(6, 6),
(6, 14),
(6, 15),
(7, 7),
(7, 14),
(7, 15),
(8, 8),
(8, 15);
