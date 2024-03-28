Project Title: SQL - More Queries

Description:
This project consists of a series of SQL scripts aimed at performing various tasks related to MySQL database management. Each script fulfills a specific requirement, such as creating users, databases, tables, and executing queries to retrieve, manipulate, and analyze data.

Table of Contents:

Installation
Usage
Scripts Overview
Tasks Description
Advanced Tasks
Credits

Installation:

To use these scripts, ensure you have MySQL installed on your system. You can download and install MySQL from the official MySQL website. Once installed, you can execute the scripts using the MySQL command-line interface or any MySQL management tool of your choice.

Usage:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the scripts.
3. Execute the desired script using the MySQL command-line interface or your preferred MySQL management tool.
4. Follow the prompts or provide any necessary arguments as mentioned in the script comments.

Scripts Overview:

>Script 0: Lists all privileges of MySQL users user_0d_1 and user_0d_2.
>Script 1: Creates the MySQL server user user_0d_1 with all privileges.
>Script 2: Creates the database hbtn_0d_2 and the user user_0d_2 with only SELECT privilege in the database.
>Script 3: Creates the table force_name with an id column and a name column that can't be null>Script 4: Creates the table id_not_null with an id column having a default value of 1 and a name column.
>Script 5: Creates the table unique_id with an id column having a default value of 1 and must be unique, and a name column.
>Script 6: Creates the database hbtn_0d_usa and the table states with an id column as a primary key and a name column.
>Script 7: Creates the database hbtn_0d_usa and the table cities with an id column as a primary key, a state_id column as a FOREIGN KEY, and a name column.
>Script 8: Lists all cities of California from the database hbtn_0d_usa.
>Script 9: Lists all cities and their corresponding states from the database hbtn_0d_usa.
>Script 10: Lists all shows with at least one genre linked from the database hbtn_0d_tvshows.
>Script 11: Lists all shows and their corresponding genre IDs from the database hbtn_0d_tvshows.
>Script 12: Lists all shows without a genre linked from the database hbtn_0d_tvshows.
>Script 13: Lists all genres and the number of shows linked to each from the database hbtn_0d_tvshows.
>Script 14: Lists all genres of the show "Dexter" from the database hbtn_0d_tvshows.
>Script 15: Lists all Comedy shows from the database hbtn_0d_tvshows.
>Script 16: Lists all shows and their corresponding genres from the database hbtn_0d_tvshows.
>Script 17: Lists all genres not linked to the show "Dexter" from the database hbtn_0d_tvshows.
>Script 18: Lists all shows without the genre Comedy from the database hbtn_0d_tvshows.
>Script 19: Lists all shows from the database hbtn_0d_tvshows_rate by their rating.
>Script 20: Lists all genres from the database hbtn_0d_tvshows_rate by their rating.

Tasks Description:

Task 0: Lists privileges of MySQL users.
Task 1: Creates a MySQL server user with all privileges.
Task 2: Creates a database and a user with SELECT privilege.
Task 3: Creates a table with a non-null name column.
Task 4: Creates a table with a default value for the id column.
Task 5: Creates a table with a unique id column.
Task 6: Creates a database and a table with an auto-generated primary key.
Task 7: Creates a database and a table with a foreign key constraint.
Task 8: Lists cities of California without using JOIN.
Task 9: Lists cities and their corresponding states using only one SELECT statement.
Task 10-20: Various data retrieval tasks from provided databases.

Advanced Tasks:

Task 17: Lists genres not linked to the show "Dexter" using a maximum of two SELECT statements.
Task 18: Lists shows without the genre Comedy using a maximum of two SELECT statements.
Task 19: Lists shows by rating from the hbtn_0d_tvshows_rate database.
Task 20: Lists genres by rating from the hbtn_0d_tvshows_rate database.

Credits:

This project was completed as part of the ALX Software Engineering program by Matthew Zakari
