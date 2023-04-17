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
