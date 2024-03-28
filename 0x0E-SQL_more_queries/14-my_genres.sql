-- Queries the hbtn_0d_tvshows database to retrieve all genres associated with the show Dexter
-- Retrieves all records from a table based on the relationship with another table
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;

