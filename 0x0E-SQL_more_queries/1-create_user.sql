-- Task: Create MySQL server user user_0d_1 with all privileges

-- Check if the user exists, and if so, drop it to avoid conflicts
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user with all privileges and set the password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

