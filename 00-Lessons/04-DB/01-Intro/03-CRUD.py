# CRUD
# c -> Create
# r -> Read
# u -> Update
# d -> Delete

# SQL Commands:
# Create -> INSERT
# Read   -> SELECT
# Update -> UPDATE
# Delete -> DELETE
# Example Table: Employees
# Columns: ID, Name, Position, Salary
# 1. Create (INSERT)
INSERT INTO Employees (ID, Name, Position, Salary) VALUES (1, 'John Doe', 'Developer', 60000);
# 2. Read (SELECT)
SELECT * FROM Employees WHERE ID = 1;
# 3. Update (UPDATE)
UPDATE Employees SET Salary = 65000 WHERE ID = 1;
# 4. Delete (DELETE)
DELETE FROM Employees WHERE ID = 1;
# Note: Always ensure to back up your data before performing Update or Delete operations.


