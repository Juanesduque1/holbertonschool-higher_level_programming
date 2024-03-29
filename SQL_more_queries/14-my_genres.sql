-- Script to list all genres of a specific TV show
SELECT a.name
FROM tv_genres AS a
JOIN tv_show_genres AS b
    ON a.id = b.genre_id
JOIN tv_shows AS c
    ON b.show_id = c.id
    WHERE c.title = 'Dexter'
ORDER BY a.name;