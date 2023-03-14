-- creates the table which will be called First_table on the current database
-- The database name will be passed as an argument of my sql command
--		id INT
--		name VARCHAR(200)
-- the database name wil be passed as an argument of mysql command
-- If the table First_table already exist, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT First_table (id INT, name VARCHAR(200));
