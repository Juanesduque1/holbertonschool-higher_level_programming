-- Script that list all genres from a database
SELECT a.name AS genre, COUNT(b.genre_id) AS number_of_shows
FROM tv_genres AS a
JOIN tv_show_genres AS b
    ON a.id = b.genre_id
GROUP BY a.name
ORDER BY number_of_shows DESC;
