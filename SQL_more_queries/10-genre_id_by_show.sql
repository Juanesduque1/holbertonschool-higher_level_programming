-- Script that lists all shows contained in database
SELECT a.title, b.genre_id
FROM tv_shows as a
JOIN tv_show_genres as b
    ON a.id = b.show_id
ORDER BY a.title, b.genre_id;
