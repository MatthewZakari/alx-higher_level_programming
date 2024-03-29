-- Retrieves all shows along with their associated genres from the hbtn_0d_tvshows database
-- Utilizes JOIN operations to connect tables and retrieve all related data
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;

