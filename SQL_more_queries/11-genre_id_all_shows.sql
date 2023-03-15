-- Script that show specific data contained in a database
SELECT a.title, b.genre_id
FROM tv_shows as a
LEFT JOIN tv_show_genres as b
    ON a.id = b.show_id
ORDER BY a.title, b.genre_id;
