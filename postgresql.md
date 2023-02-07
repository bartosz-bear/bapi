# PostgreSQL

<https://www.datacamp.com/tutorial/beginners-introduction-postgresql>

## Syntax

Keywords are not case-sensitive in SQL, but data is.

## KEYWORDS

`SELECT` field/column

`FROM` table

```sql
SELECT name, card_number FROM patrons;
```

```sql
SELECT * FROM patrons;
```

## IDENTIFIERS

Identifier is a name of a particular part of a database (table name, field name).

Identifiers are always lower case.

## ALIASING

```sql
SELECT name AS first_name, year_hired
FROM employees;
```

`name` is a name of a field in a table, while `first_name` will be a name of the field in the result set

## CREATING A DATABASE

## DATABASE DESIGN QUESTIONS

1. What kind of thing are we storing?

cities

2. What properties does this thing have?

name, country, population, area

3. What type of data does each of those properties contain?

name (string)
country (string)
population (number)
area (number)

## CREATING A TABLE

```sql
CREATE TABLE cities (
  name VARCHAR(50),
  country VARCHAR(50),
  population INTEGER,
  area INTEGER
);
```

Creating a table with auto-increment primary key.

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50)
);
```

Creating a table with a foreign key

```sql
CREATE TABLE photos (
  id SERIAL PRIMARY KEY,
  url VARCHAR(200),
  user_id INTEGER REFERENCES users(id)
);
```

## DELETING A TABLE

```sql
DROP TABLE photos;
```

## INSERTING DATA

- actual values are matching in the exact order of specified fields

```sql
INSERT INTO cities (name, country, population, area)
VALUES ('Tokyo', 'Japan', 38505000, 8223);
```

## INSERTING SEVERAL ROWS AT THE TIME

```sql
INSERT INTO cities (name, country, population, area)
VALUES
	('Delhi', 'India', 28125000, 2240),
  ('Shanghai', 'China', 22125000, 4015),
  ('Sao Paulo', 'Brazil', 20935000, 3043);
```

## SELECTING DISTINCT RECORDS

```sql
SELECT DISTINCT year_hired
FROM employees;
```

## SELECTING A DISTINCT COMBINATION OF TWO FIELDS

```sql
SELECT DISTINCT dept_id, year_hired
FROM employees;
```

## VIEWS

View is a virtual table that is the result of a saved SQL `SELECT` statement

Result set is not stored in the database. Views (saved queries) are stored.

Views automatically update in response to updates in the underlying data.

```sql
CREATE VIEW employee_hire_years AS
SELECT id, name, year_hired
FROM employees;
```

While a view is created, we can query is as it was a normal table.

```
SELECT id, name
FROM employee_hire_years;
```

## RESULT SET

Result set is a result of a query.

## CALCULATED COLUMNS

```sql
SELECT name, population / area AS density
FROM cities;
```

### OPERATORS FOR CALCULATED COLUMNS

- +
- -
- *
- /
- ^ (exponent)
- |/ (square root)
- @ (absolute value)
- % (remainder)

```sql
SELECT @area AS density FROM cities;
```

```sql
SELECT |/area AS density FROM cities;
```

## STRING OPERATORS AND FUNCTIONS

- || - join two strings
- CONCAT() - join two strings
- LOWER() - gives a lower case string
- LENGTH() - gives number of characters in a string
- UPPER() - gives and upper case string

## CONCATANATING STRINGS

```sql
SELECT name || ' ' || country
FROM cities;
```

```sql
SELECT CONCAT(name, ' ', country) AS location
FROM cities;
```

## UPPER()

```sql
SELECT UPPER(name) FROM cities;
```

```sql
SELECT CONCAT(UPPER(name), ' ', UPPER(country)) AS location FROM cities;
```

```sql
SELECT
  UPPER(CONCAT(name, ' ', country)) AS location
FROM
  cities;
```

## COUNT()

```sql
SELECT COUNT(birthdate) AS count_birthdates
FROM people;
```

```sql
SELECT COUNT(name) AS count_names, COUNT(birthdate) AS count_birthdates
FROM people;
```

## COUNT(*) TOTAL NUMBER OF RECORDS IN A TABLE

```sql
SELECT COUNT(*) AS total_records
FROM people;
```

## COUNT() WITH DISTINCT

- excludes duplicates

```sql
SELECT COUNT(DISTINCT birthdate) AS count_distinct_birthdates
FROM people;
```

## FILTERING WITH WHERE()

- it works like Excel filter

```sql
SELECT *
FROM tutorial.us_housing_units
WHERE month = 1
```

Order of filtering:

- FIRST: `FROM cities`
- SECOND: `WHERE area > 4000`
- THIRD: `SELECT name`

## WHERE COMPARISON OPERATORS

- `=` (comparison using single equal sign)
- `>`
- `<`
- `>=`
- `<=`
- `IN` (values present in a list)
- `<>` (not equal)
- `!=` (not equal)
- `BETWEEN` (values between two numbers)
- `NOT` (values not present in a list)

## `BETWEEN` OPERATOR

```sql
SELECT name, area
FROM cities
WHERE area BETWEEN 2000 AND 4000;
```

## `IN` AND `NOT IN` OPERATORS

```sql
SELECT name, area
FROM cities
WHERE
  name IN ('Tokyo', 'Shanghai');
```

```sql
SELECT name, area
FROM cities
WHERE
  name NOT IN ('Delhi', 'Tokyo');
```

## COMBINING `NOT IN` AND `AND`

Filter for all records where area IS NOT 8223 or 3044 AND where name of the city is Dehli.

```sql
SELECT
  name,
  area
FROM
  cities
WHERE
  area NOT IN (8223, 3044) AND name = 'Delhi';
```

We can chain as many AND, OR statements as well like.

```sql
SELECT
  name,
  area
FROM
  cities
WHERE
  area NOT IN (8223, 3043)
  OR name = 'Delhi'
  OR name = 'Tokyo';
```

## COMBINING CALCULATED COLUMNS WITH `WHERE` CLAUSE

```sql
SELECT
  name,
  population / area AS population_density
FROM
  cities
WHERE
  population / area > 6000;
```

## UPDATING RECORDS

```sql
UPDATE cities
SET population = 3505000
WHERE name = 'Tokyo';
```

## DELETING RECORDS

```sql
DELETE FROM cities
WHERE name = 'Tokyo';
```

## ORDER OF QUERY EXECUTION

- it's important to know query order for debugging and aliasing purposes

1. TABLE SELECTION (`FROM people`)
2. FIELDS SELECTION (`SELECT name`)
3. SUBSELECTION OF A RESULT SET (`LIMIT 10`)

## ALIAS DECLARATION AND REFERENCING

Aliases can only be referenced by a futher code if the alias was declared earlier on in the code.

## DEBUGGING SQL

- Incorrect or missing punctuation, especially a comma error is a very common error
- Misspelling
- Incorrect capitalisation

## SQL FORMATTING

- new lines, capitalization, indentation and semi-colons are not required in SQL

```sql
select title, release_year, country from films limit 3
```

<https://www.sqlstyle.guide/>

## SQL BEST PRACTICES

- capitalized keywords
- new lines between keywords
- indentations for multiple fields
- using semi-colons at the end of query
- using lowercase letters only for table and field names
- using underscore instead of space for table and field names

## DEALING WITH NON-STANDARD FIELD NAMES

```sql
SELECT title, "release year", country
FROM films
LIMIT 3;
```

## Conventions

Table names and field names should be named using small letters only and underscores. Table names should be called using plurals and field names using singulars.

`customers`

`customer_name`

## Data Types

Data types are SQL implementation based (eg. different in PostreSQL and MySQL).

<https://www.postgresql.org/docs/current/datatype.html>

## POSTGRESQL DATA TYPES

## VARCHAR

- variable length character

```sql
VARCHAR(50)
```

## INTEGER

- signed integer number
- from -2.1B to 2.1B

## NULL

- no value, nothing

## Collation

Collation specifies how data is sorted and compared in a database. Collation provides the sorting rules, case and accent sensitivity properties for the data in the database.

For example, when you run a query using the `ORDER BY` clause, collation determines whether or not uppercase letters and lowercase letters are treated the same.

## SERIAL

`SERIAL` in PostgresSQL lets you create an auto-increment column. By default, it creates values of type integer. It is a good practice to use auto-increments for primary keys.

## PRIMARY KEY

Primary key uniquely identifies each record in a particular table.

- each row in every table has one primary key
- not other row in the same table can have the same primary key
- 99% of the time primary key is called `id`
- either an integer or a UUID
- will never change

## FOREIGN KEY

Foreign key identifies a record (usually in an another table) that this row is associated with. Foreign key in table A is a primary key in table B.

- in one-to-many relationship, the 'many' side of the relationship gets the foreign key column
- rows only have a foreign key if they 'belong' to another record in a different table
- many rows in the same table can have the same foreign key
- name of a foreign key varies, usually they are called something like `user_id` or `department_id`
- foreign keys are referring to concrete primary keys in a different table
- foreign keys will change when a relationship changes (eg. an employee changes a department)

## GENERAL STRUCTURE OF A TABLE CREATION QUERY IN POSTGRESQL

```postgresql
CREATE TABLE table_name (
  column_name TYPE column_constraint,
  table_constraint table_constraint
)
```

## EXAMPLE

```postgresql
CREATE TABLE datacamp_courses(
 course_id SERIAL PRIMARY KEY,
 course_name VARCHAR (50) UNIQUE NOT NULL,
 course_instructor VARCHAR (100) NOT NULL,
 topic VARCHAR (20) NOT NULL
);
```

## INSERTING RECORDS

```postgresql
INSERT INTO datacamp_courses(course_name, course_instructor, topic)
VALUES('Deep Leaning in Python', 'Dan Becker', 'Python');

INSERT INTO datacamp_courses(course_name, course_instructor, topic)
VALUES('Joining Data in PostreSQL', 'Chester Ismay', 'SQL');
```

## QUERING DATA

```postgresql
SELECT * FROM datacamp_courses;
```

```postgresql
SELECT course_name, topic from datacamp_courses;
```

## UPDATING RECORDS

```postgresql
UPDATE table_name SET column_name = 'Joining Data in SQL'
WHERE another_column_name = 'Chester Ismay'
```

## DELETING RECORDS

```postgresql
DELETE from datacamp_courses
WHERE course_name = 'Deep Learning in Python';
```

## `\dt` - SHOW TABLES COMMAND LINE

```
\dt
```

# DATABASE RELATIONSHIPS

There are 4 different kinds of relationships

## one-to-one relationship

One record of the first table will be linked to zero or one records of second table.

Eg. each employee in the `Employee` table will have a corresponding row in `EmployeeDetails` table that stores the current personal details of an employee. So each employee will have zero or on record in `EmployeeDetails` table.

![](./images/postgresql/one-to-one.png)

`EmployeeID` is a PRIMARY KEY in `Employee` table and a FOREIGN KEY in the `EmployeeDetails` table.

Each employee has either one or zero records in the `EmployeeDetails' table.

![](./images/postgresql/one-to-one2.png)

## one-to-many relationship

- one-to-many is the most common among tables relationships
- a single column from one table can be linked to zero or more columns in another table
- 'employee has many addresses'

`Employee` table stores employee records. `Address` table stores adresses of employees. Each employee will have only one record in the `Employee` table but it can have zero, one or several records in `Address` table. This is because each employee can have zero, one or several addresses (Home address, Office address, Vacations address).

![](./images/postgresql/one-to-many2.png)

`Employee` table and `Address` table are linked by the key column `EmployeeID`'. `EmployeeId` is a primary key in `Employee` table and a foreign key in `Address` table.

In one-to-many relationship, the 'many' side of the relationship gets the foreign key column

![](./images/postgresql/one-to-many.png)

## many-to-one relationship

- vice versa of one-to-many relationship
- 'many addresses belong to one employee'
- 'many employees work in one department'

## many-to-many relationship

- many-to-many relationship allows you to relate each row in one table to many rows in another table, and vice versa
- eg. an employee can have many skills, and a particular skill can be associated with one or more employees

Many-to-many relationship is created using a JUNCTURE TABLE. `EmployySkill` is a junction table that contains `EmployeeID` and `SkillID` as foreign key columns, which allow formation of many-to-many relationship between `Employee` and `SkillDescription` tables.

Indivindually, the `Employee` and `EmployeeSkill` have a one-to-many realtionship and `SkillDescription` and `EmployeeSkill` also have one-to-many relationship. But, they form form many-to-many relationshipo using a juncture table `EmployeeSkill`.

![](./images/postgresql/many-to-many.png)


![](./images/postgresql/many-to-many2.png)

<https://www.tutorialsteacher.com/sqlserver/tables-relations>

## What is a DATABASE SCHEMA?

Database schema is the organization and structure of a database. A schema contains schema objects, which could be tables, fields, data types, views, stored procedures, relationships, primary keys, foreign keys, etc.

![](./images/postgresql/database_schema.png)

## FOREIGN KEY CONSTRAINT ERROR DURING INSERTION

This error pops up when we try to enter a record with a foreign key, and the foreign key specified by us doesn't exist as a primary key in a different table.

```sql
INSERT INTO photos (ulr, user_id)
VALUES ('http://df.jpg', 999);
```

This query will results in an error because there is no user with `id` 999.

`insert or update on table "photos" violates foreign key constraint "photos_user_id_fkey"`

## FOREIGN KEY CONSTRAINT ERROR DURING DELETION

```sql
DELETE FROM users
WHERE id = 1;
```

`update or delete on table "users" violates foreign key constraint "photos_user_id_fkey" on table "photos"`

## DATA CONSISTENCY DURING INSERTION 

We are not allowed to add a record with a foreign key when this foreign key doesn't exist as a primary key in a different table.

However, we are allowed to insert a record with a `NULL` value as a foreign key.

## DATA CONSISTENCY DURING DELETION

- we can `ON DELETE` parameter to define a default behavior of the records with foreign key, in case records with the corresponding primary keys are being deleted

```sql
CREATE TABLE photos (
  id SERIAL PRIMARY KEY,
  url VARCHAR(200),
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
```

`ON DELETE RESTRICT` - throw an error

`ON DELETE NO ACTION` - throw an error

`ON DELETE CASCADE` - delete the corresponding items in the second table Eg. when you delete a post in a blog, you also want to delete all corresponding comments on that post.

`ON DELETE SET NULL` - change foreign key values to `NULL`. Eg. when a user wants to delete his account but we want to keep his photos (in case he changes his mind in the future).

`ON DELETE SET DEFAULT` - change foreign key values to a default value, if one is provided

## `JOINS` AND AGGREGATIONS

## `JOINS`

- produce values by merging together rows from multiple (minimum 2) related tables
- use joins most of the times when you're asked to find data that involves multiple resources
- during `JOIN` operation an additional, virtual table is created which constists all rows of the selected table, merged together using a primary and a foreign key
- in the last step, the virtual table is stripped of all fields but the ones defined in the `SELECT` statement
- when there is no match between a foreign key and a primary key for a particular record, this record is not added to the results set

## AGGREGATIONS

- aggregations take several rows and calculate a single value (like `groupBy` in `pandas` )
- keywords like `most`, `average`, `least` are examples of aggregations

## `JOINS` SYNTAX

```sql
SELECT contents, url
FROM comments
JOIN photos ON photos.id = comments.photo_id;
```

- in the `SELECT` statement we select fields from BOTH tables
- in the `FROM` statement we specify the first table (the one with a foreign key)
- in the `JOIN` statement we specify the second table (the one with a primary key which is referenced by a foreign key of the first table)
- in the `ON` statement we define the primary key of the second table first, and then a foreign key in the first table

## ALTERNATE FORMS OF `JOINS` SYNTAX

- sometimes it makes a difference which table is defined first and which is defined as a second, and sometimes it doesn't

## PRECISE FIELD REFERENCING SYNTAX

- `id` field exists in both tables (photos and comments), therefore in order to avoid an error we must specify which field (from which table) we are looking for

```sql
SELECT photos.id
FROM photos
JOIN comments ON photos.id = comments.photo_id;
```

## RENAMING FIELD NAMES FOR EXTRA PRECISION

```sql
SELECT comments.id AS comments_id, photos.id AS photos_id
FROM photos
JOIN comments ON photos.id = comments.photo_id;
```

## RENAMING TABLE REFERENCES

- if a table is renamed, it can be refered with a new name already in the same query
- good practice

```sql
SELECT comments.id, p.id
FROM photos AS p
JOIN comments ON p.id = comments.photo_id;
```

## ALTERNATIVE SYNTAX FOR TABLE RENAMING

- bad practice

```sql
SELECT comments.id, p.id
FROM photos p
JOIN comments ON p.id = comments.photo_id;
```

## ERROR: `COLUMN REFERENCE "ID" IS AMBIGOUS`

`COLUMN REFERENCE "ID" IS AMBIGOUS` happens when two tables have the same field name and it's not clear which field we are refering to in our query.

## FOUR TYPES OF `JOINS`

## `INNER JOIN`

- this is a default `JOIN`
- `JOIN` is equal to `INNER JOIN`
- when there is no match between a foreign key and a primary key, the record will not be included in the result set

```sql
SELECT url, username
FROM photos
JOIN users ON users.id = photos.user_id;
```

![](./images/postgresql/inner_join.png)

## `LEFT OUTER JOIN`

- when there is no match between a foreign key and a primary key, the record from the FIRST (LEFT) table (the one defined in the `FROM` statement) will be included in the set, and the rest of the fields in the result set will be populated with `NULL` values
- order of the tables defined in the query MATTERS, switching tables will give different results

```sql
SELECT url, username
FROM photos
LEFT JOIN users ON users.id = photos.user_id;
```

![](./images/postgresql/left_outer_join.png)

## `RIGHT OUTER JOIN`

- when there is no match between a foreign key and a primary key, the record from the SECOND (RIGHT) table (the one defined in the `JOIN` statement) will be included in the set, and the rest of the fields in the result set will be populated with `NULL` values
- order of the tables defined in the query MATTERS, switching tables will give different results


```sql
SELECT url, username
FROM photos
RIGHT JOIN users ON users.id = photos.user_id;
```

![](./images/postgresql/right_outer_join.png)

## `FULL JOIN`

- when there is no match between a foreign key and a primary key, both records from both tables will be included as two separate records, and the rest of the fields of the added records will be populated with `NULL` value

```sql
SELECT url, username
FROM photos
FULL JOIN users ON users.id = photos.user_id;
```

![](./images/postgresql/full_join.png)

## COMBINING `WHERE` WITH `JOIN`

```sql
SELECT ulr, contents
FROM comments
JOIN photos ON photos.id = comments.photo_id
WHERE comments.user_id = photos.user_id;
```



## THREE-WAY `JOINS`

```sql
SELECT url, contents, username
FROM comments
JOIN photos ON photos.id = comments.photo_id
JOIN users ON users.id = comments.user_id AND users.id = photos.user_id
```

## GROUPING AND AGGREGATE FUNCTIONS

## GROUPING USING `GROUP BY`

- `GROUP BY` finds a set of UNIQUE records for a given field and creates groups (buckets) for each of these unique items
- if there are several records for a particular group, these records are grouped into a subset and they are available from within the group
- essentially, `GROUP BY` creates a new table but the number of records and its contents remain the same, the only thing which changes is the order of the records within the result set 

Before

![](./images/postgresql/group_by_before.png)

After

![](./images/postgresql/group_by_after.png)


In `GROUP BY` we can only DIRECTLY select the same field which we define in `GROUP BY` clause. If we want to use other fields we need to use an AGGREGATE function.

Example

This is fine, because user_id is used twice

```sql
SELECT user_id
FROM comments
GROUP BY user_id;
```

And this one is going to raise an error:

```sql
SELECT contents
FROM comments
GROUP BY user_id;
```

## SQL FLAVORS

Standard keywords are the same for all SQL flavors. Only additional keywords on top of the standard set of keywords, make SQL flavors unique.

Difference between different SQL flavors is similar to differences between British and American English.

PostgresSQL

```sql
SELECT id, name
FROM employees
LIMIT 2;
```

SQL Server

```sql
SELECT id, name
FROM employees
TOP 2;
```

## LEARNING

Basic: Datacamp, Introduction to SQL

Intermediate: Udemy, SQL & Database Design A-Z
<https://www.udemy.com/course/sqldatabases/?LSNPUBID=JVFxdTr9V80&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-YaWKvZjwH58FdJLO_nQI4g&utm_medium=udemyads&utm_source=aff-campaign>

Intermediate: Mode Intermediate SQL

<https://mode.com/sql-tutorial/intro-to-intermediate-sql/>

Advanced: Advanced SQL for Query Tuning and Performance Optimization

<https://www.linkedin.com/learning/advanced-sql-for-query-tuning-and-performance-optimization>

Advanced: High Performance SQL

<https://vladmihalcea.teachable.com/p/high-performance-sql-online?coupon_code=HPSQLV150OFF&affcode=172599_kuoszt8s>

COMPLETE: Beginner to Advanced

<https://www.udemy.com/course/sql-and-postgresql/>

SQL Style Guide

<https://www.sqlstyle.guide/>

Diagrams

<https://www.diagrams.net/>

PostgresSQL Online

<https://www.pg-sql.com>