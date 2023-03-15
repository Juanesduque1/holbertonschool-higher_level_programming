-- Script that lists all comedy shows in the database
SELECT a.title
FROM tv_shows AS a
JOIN tv_show_genres as b
    ON a.id = b.show_id
JOIN tv_genres as c
    ON b.genre_id = c.id
    WHERE c.name = 'Comedy'
ORDER BY a.title;
