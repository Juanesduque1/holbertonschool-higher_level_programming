-- Script that lists all shows contained in a database without a genre
SELECT a.title, b.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS b
    ON a.id = b.show_id
    WHERE b.genre_id is NULL
ORDER BY a.title, b.genre_id;
