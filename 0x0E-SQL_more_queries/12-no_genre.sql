-- Retrieve all shows from the hbtn_0d_tvshows database that do not have an associated genre.
-- Retrieve all records from two tables where a specific column is not linked.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

