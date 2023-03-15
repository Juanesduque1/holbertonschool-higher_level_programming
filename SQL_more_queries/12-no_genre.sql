-- Script that lists all shows contained in a database without a genre
SELECT a.title, b.genre_id
FROM tv_shows as a
LEFT JOIN tv_show_genres as b
    ON a.id = b.show_id
    WHERE b.genre_id is NULL
ORDER BY a.title, b.genre_id;
