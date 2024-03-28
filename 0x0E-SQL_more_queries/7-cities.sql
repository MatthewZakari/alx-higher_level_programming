-- Create a new database named 'hbtn_0d_usa' and a table named 'cities' within it on your MySQL server
-- Script to create a database and its associated table

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the created database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

