#DQL - Used to query data from the database
SELECT column1, column2 FROM table_name WHERE condition;

#DML - Used to manipulate data within the database
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
UPDATE table_name SET column1 = value1 WHERE condition;
DELETE FROM table_name WHERE condition;

#DDL - Used to define and modify database structures
CREATE TABLE table_name (
    column1 datatype,...)
ALTER TABLE table_name ADD column_name datatype;
DROP TABLE table_name;

#DCL - Used to control access to data within the database
CREATE USER user_name IDENTIFIED BY password;
REVOKE SELECT ON table_name FROM user_name; -- Revokes specific privileges from a user
GRANT SELECT ON table_name TO user_name; -- Grants specific privileges to a user

#DTL - Used to define and manage data types within the database
CREATE TYPE type_name AS OBJECT (
    attribute1 datatype,
    attribute2 datatype
);
BEGIN TRANSACTION; -- Starts a new transaction
COMMIT; -- Saves all changes made during the current transaction
ROLLBACK; -- Undoes all changes made during the current transaction

#TCL - Used to manage transactions in the database
SAVEPOINT savepoint_name; -- Sets a savepoint within a transaction
SET TRANSACTION; -- Sets the characteristics for the current transaction
END TRANSACTION; -- Ends the current transaction
TRUNCATE TABLE table_name;


