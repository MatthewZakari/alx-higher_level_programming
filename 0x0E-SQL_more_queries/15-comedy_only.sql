-- Retrieves all genres associated with the TV show "Dexter" from the hbtn_0d_tvshows database.
-- Retrieves all Comedy TV shows from the hbtn_0d_tvshows database.
-- Retrieves all rows from a database corresponding to a specific column value.

SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;

