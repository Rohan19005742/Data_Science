# Keys in Relational Model

- keys are fundamental components on ensure unquieness of rows.
- It also helps with efficient data retrieval

## Types of Database keys

### Super Key
- A set of one or more attributes that can uniquely identfy a row.
- It can contain extra attributes that are not necessary for uniquness.

### Candidate Key
- The minimal set of attributes that can uniquely identify a row. (minimal super key)

### Primary key
- There can be more than 1 candidate key, from which one is choosen to be a primary key.
- Primary keys are not null, they are unique and it doesnt have to consist of a single column (could be a composite primary key).

### Alternate Key (secondary key)
- Any candidate key in a table that is not chosen as the primary key.

### Foreign key
- Is an attribute in one table that refers ot the primary key in another table.

### Composite Key
- combination of 2 or more attributes yo uniquely identify all rows.