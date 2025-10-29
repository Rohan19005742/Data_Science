# Sql Commands

### Select
- Lets you choose which attributes you want the data from.

### Distinct
```
SELECT DISTINCT name
FROM customers;
```
- lets you choose unique values for the attribute

### Into
```
SELECT * INTO customers
FROM customers_backup;
```

- lets you copy data from one table into another

### Top
```
SELECT TOP 50 * FROM customers;

SELECT TOP 50 PERCENT * FROM customers;
```

- lets you select the top x number or percent of result.

### As

- renames a column / table with an alias we choose.

### FROM
- lets us choose which table we want to retrieve the data from.

### WHERE
- allows you to filter your query to only return results that match a set of conditions.

### AND

- combines 2 or more conditions in a single query, all of the conditions must be met for result to be returned

### OR

- combines 2 or more conditions in a single query, only 1 of the conditions must be met for result to be returned

### Between

```
SELECT name
FROM customers
WHERE age BETWEEN 45 AND 55;
```

- filters your query to return only results that fit a specified range.

- begin and end values are included.

### Like
- searches for a specified pattern in a column.
```
SELECT name
FROM customers
WHERE name LIKE ‘%Bob%’;
```

%x — will select all values that begin with x

%x% — will select all values that include x

x% — will select all values that end with x

x%y — will select all values that begin with x and end with y

_x% — will select all values have x as the second character

x_% — will select all values that begin with x and are at least two characters long. You can add additional _ characters to extend the length requirement, i.e. x___%

### In

```
SELECT name
FROM customers
WHERE name IN (‘Bob’, ‘Fred’, ‘Harry’);
```

- allows us to specify multiple values we want to select for when using the WHERE command.


### IS NULL

- checks if a data is null

### IS NOT NULL

- check if data is not null

### CREATE

- can be used to setup a database, table, index or view

### CREATE INDEX

- can be used for efficient searching.
```
CREATE INDEX idx_dept ON employees(department);
```
Index: idx_dept

"Finance" → [Row 2, Row 3]
"HR"      → [Row 1]
"IT"      → [Row 4]

so when you try to select a department, it knows which rows to go to stright away.


### CREATE VIEW

CREATE VIEW creates a virtual table based on the result set of an SQL statement. A view is like a regular table (and can be queried like one), but it is not saved as a permanent table in the database.


### DROP
DROP statements can be used to delete entire databases, tables or indexes.

