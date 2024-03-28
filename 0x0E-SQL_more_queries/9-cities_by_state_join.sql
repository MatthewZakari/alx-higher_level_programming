-- Retrieve a list of all cities from the database hbtn_0d_usa
-- Retrieve all records from a specific column across multiple tables in a database
SELECT cities.id, cities.name, states.name AS state_name 
FROM cities 
LEFT JOIN states ON states.id = cities.state_id 
ORDER BY cities.id;

