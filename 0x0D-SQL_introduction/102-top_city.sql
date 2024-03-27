-- Display the top 3 cities by average temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8) -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3; -- Limit the result to top 3 cities

