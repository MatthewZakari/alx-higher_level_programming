-- Retrieves all shows from the hbtn_0d_tvshows_rate table ordered by their ratings.
-- Retrieves all records from a table, summing up the linked rows accordingly.

SELECT title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;

