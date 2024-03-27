-- List all records of the table second_table of the database hbtn_0c_0
-- Only list rows with a name value
-- Display score and name, ordered by descending score

SELECT score, name FROM second_table
WHERE `name` != ""
ORDER BY score DESC;

