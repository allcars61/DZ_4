-- Название и год выхода альбомов, вышедших в 2018 году.
SELECT title, year FROM albums WHERE year = 2018;

-- Название и продолжительность самого длительного трека.
SELECT title, duration FROM tracks ORDER BY duration DESC LIMIT 1;

-- Название треков, продолжительность которых не менее 3,5 минут.
SELECT title FROM tracks WHERE duration >= 210;

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT title FROM collections WHERE year BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова.
SELECT name FROM artists WHERE name NOT LIKE '% %';

-- Название треков, которые содержат слово «мой» или «my».
SELECT title FROM tracks WHERE title ILIKE '%мой%' OR title ILIKE '%my%';

-- Количество исполнителей в каждом жанре.
SELECT genres.name AS genre, COUNT(artists.id) AS artists_count
FROM genres
LEFT JOIN artists ON artists.genre_id = genres.id
GROUP BY genres.name;

-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(tracks.id) AS tracks_count
FROM tracks
JOIN albums ON albums.id = tracks.album_id
WHERE albums.year BETWEEN 2019 AND 2020;

-- Средняя продолжительность треков по каждому альбому.
SELECT albums.title AS album, AVG(tracks.duration) AS avg_duration
FROM albums
JOIN tracks ON tracks.album_id = albums.id
GROUP BY albums.title;

-- Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT artists.name
FROM artists
LEFT JOIN albums ON albums.artist_id = artists.id
WHERE albums.year != 2020 OR albums.year IS NULL;

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT collections.title
FROM collections
JOIN collection_tracks ON collection_tracks.collection_id = collections.id
JOIN tracks ON tracks.id = collection_tracks.track_id
JOIN albums ON albums.id = tracks.album_id
JOIN artists ON artists.id = albums.artist_id
WHERE artists.name = 'Queen';

-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT ct.title
FROM collections ct
JOIN collection_tracks ctr ON ct.id = ctr.collection_id
JOIN tracks t ON ctr.track_id = t.id
JOIN albums a ON t.album_id = a.id
JOIN artists ar ON a.artist_id = ar.id
WHERE ar.id IN (
  SELECT ar2.id
  FROM artists ar2
  GROUP BY ar2.id
  HAVING COUNT(DISTINCT ar2.genre_id) > 1
)
GROUP BY ct.id
HAVING COUNT(DISTINCT ar.genre_id) > 1;

-- Наименования треков, которые не входят в сборники.
SELECT tracks.title
FROM tracks
LEFT JOIN collection_tracks ON collection_tracks.track_id = tracks.id
WHERE collection_tracks.track_id IS NULL;

-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT artists.name, tracks.title, tracks.duration
FROM artists
JOIN albums ON albums.artist_id = artists.id
JOIN tracks ON tracks.album_id = albums.id
WHERE tracks.duration = (SELECT MIN(duration) FROM tracks);

-- Названия альбомов, содержащих наименьшее количество треков.
SELECT albums.title, COUNT(tracks.id) AS tracks_count
FROM albums
JOIN tracks ON tracks.album_id = albums.id
GROUP BY albums.title
ORDER BY tracks_count
LIMIT 1;
