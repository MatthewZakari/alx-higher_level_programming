-- Retrieves all TV shows from the hbtn_0d_tvshows database that are associated with at least one genre.
-- Retrieves all records from a database where there is a common column among them.

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
INNER JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

