#	SQL - More queries

Here are some more SQL queries covering a variety of scenarios:


##Select All Columns from a Table:

SELECT * FROM table_name;


##Select Specific Columns from a Table:

SELECT column1, column2 FROM table_name;


##Filter Rows with WHERE Clause:

SELECT * FROM table_name WHERE condition;


##Sorting with ORDER BY:

SELECT * FROM table_name ORDER BY column_name ASC; -- or DESC for descending order


##Limiting Results with LIMIT:

SELECT * FROM table_name LIMIT 10;


##Filtering and Sorting Together:

SELECT * FROM table_name WHERE condition ORDER BY column_name;


##Aggregate Functions (e.g., SUM):

SELECT SUM(column_name) FROM table_name;


##Grouping Data with GROUP BY:

SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;


##Filter Groups with HAVING Clause:

SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > 1;


##Joins - INNER JOIN:

SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;


##Joins - LEFT JOIN:

SELECT * FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;


##Uniqueness with DISTINCT:

SELECT DISTINCT column_name FROM table_name;


##Inserting Data into a Table:

INSERT INTO table_name (column1, column2) VALUES (value1, value2);


##Updating Data in a Table:

UPDATE table_name SET column1 = value1 WHERE condition;


##Deleting Data from a Table:

DELETE FROM table_name WHERE condition;


##Creating a New Table:

CREATE TABLE new_table (
  column1 datatype,
  column2 datatype,
  ...
);


##Altering Table Structure:

ALTER TABLE table_name ADD new_column datatype;


## Deleting a Table:

DROP TABLE table_name;


These queries cover a range of basic and more advanced SQL operations. Depending on the specific database you're using (e.g., MySQL, PostgreSQL, SQLite), syntax might vary slightly, but these are standard SQL queries that are widely applicable. Always be cautious when executing commands that modify or delete data, especially in a production environment.





