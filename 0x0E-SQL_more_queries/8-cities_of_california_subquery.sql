-- Retrieve the names of cities located in California from the database hbtn_0d_usa
-- Selects all entries from a specific column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

