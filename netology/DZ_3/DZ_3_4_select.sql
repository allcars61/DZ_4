-- Количество исполнителей в каждом жанре.
SELECT genres.name, COUNT(artist_genres.artist_id) AS artist_count FROM genres
LEFT JOIN artist_genres ON genres.id = artist_genres.genre_id
LEFT JOIN artists ON artist_genres.artist_id = artists.id
GROUP BY genres.name;

-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(tracks.id) AS track_count FROM tracks
LEFT JOIN albums ON tracks.album_id = albums.id
WHERE albums.year BETWEEN 2019 AND 2020;


-- Средняя продолжительность треков по каждому альбому.
SELECT albums.title, AVG(tracks.duration) AS avg_duration FROM albums
LEFT JOIN tracks ON albums.id = tracks.album_id
GROUP BY albums.title;

-- Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT artists.name FROM artists
WHERE artists.name NOT IN (
    SELECT artists.name FROM artists
    JOIN album_artists ON artists.id = album_artists.artist_id
    JOIN albums ON album_artists.album_id = albums.id
    WHERE albums.year = 2020
)
GROUP BY artists.name;

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
-- группировка используется в данном запросе для исключения повторений названий сборников,
--в которых присутствует исполнитель Queen. Если бы не было группировки, то в результате
--запроса могли бы быть дубликаты названий сборников, что было бы нежелательно.
--Таким образом, группировка в данном запросе не является агрегирующей, но необходимой для
--корректного отображения результата.
SELECT collections.title FROM collections
LEFT JOIN collection_tracks ON collections.id = collection_tracks.collection_id
LEFT JOIN tracks ON collection_tracks.track_id = tracks.id
LEFT JOIN albums ON tracks.album_id = albums.id
LEFT JOIN album_artists ON albums.id = album_artists.album_id
LEFT JOIN artists ON album_artists.artist_id = artists.id
WHERE artists.name = 'Queen'
GROUP BY collections.title;


-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT DISTINCT albums.title
FROM albums
JOIN album_artists ON albums.id = album_artists.album_id
JOIN artists ON album_artists.artist_id = artists.id
JOIN artist_genres ON artists.id = artist_genres.artist_id
GROUP BY albums.id, artists.id
HAVING COUNT(DISTINCT artist_genres.genre_id) > 1;

-- Наименования треков, которые не входят в сборники.
SELECT tracks.title FROM tracks
LEFT JOIN collection_tracks ON tracks.id = collection_tracks.track_id
WHERE collection_tracks.collection_id IS NULL;

-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT artists.name FROM artists
LEFT JOIN album_artists ON artists.id = album_artists.artist_id
LEFT JOIN albums ON album_artists.album_id = albums.id
LEFT JOIN tracks ON albums.id = tracks.album_id
WHERE tracks.duration = (
    SELECT MIN(duration) FROM tracks
);

-- Названия альбомов, содержащих наименьшее количество треков.
SELECT albums.title FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP BY albums.id
HAVING COUNT(tracks.id) = (
    SELECT COUNT(*)
    FROM tracks
    GROUP BY album_id
    ORDER BY COUNT(*) ASC
    LIMIT 1
);
