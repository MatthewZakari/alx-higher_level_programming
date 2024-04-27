-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;

-- Create the 'states' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert unique state names into the 'states' table
INSERT IGNORE INTO states (name) VALUES 
("California"), 
("Arizona"), 
("Texas"), 
("New York"), 
("Nevada");

-- Delete duplicate entries from the 'states' table
DELETE s1
FROM states s1
JOIN states s2 ON s1.name = s2.name AND s1.id > s2.id;

