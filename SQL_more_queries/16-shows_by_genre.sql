-- Script that lists all shows and all genres linked to that show in a database
SELECT a.title, c.name
FROM tv_shows as a
LEFT JOIN tv_show_genres as b
    ON a.id = b.show_id
LEFT JOIN tv_genres as c
    ON b.genre_id = c.id
ORDER BY a.title, c.name;
