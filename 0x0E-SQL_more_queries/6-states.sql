-- This script creates a database named 'hbtn_0d_usa' and within it, creates a table named 'states' on your MySQL server.
-- Create the 'hbtn_0d_usa' database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'states' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);

