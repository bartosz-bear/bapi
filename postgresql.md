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

## KEYWORDS ORDER

1. `FROM` - specifies a starting table to work with
2. `JOIN` - merges data from multiple tables
3. `WHERE` - filters the set of rows
4. `GROUP BY` - groups rows by a unique set of values
5. `HAVING` - filters the set of groups

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

## UPDATING `NULL` VALUES

```sql
UPDATE products
SET price = 9999
WHERE price IS NULL;
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

## CONVENTIONS

Table names and field names should be named using small letters only and underscores. Table names should be called using plurals and field names using singulars.

`customers`

`customer_name`

## DATA TYPES


Data types are SQL implementation based (eg. different in PostreSQL and MySQL).

<https://www.postgresql.org/docs/current/datatype.html>

## POSTGRESQL DATA TYPES

## NUMERIC DATA TYPES

![](./images/postgresql/numeric_data_types.png)

## `INTEGER`

- signed integer number
- from -2.1B to 2.1B
- both negative and positive numbers who have no decimal points

## `SERIAL`

- positive sign integer from 1 to 2.1B
- positive sign numbers who have no decimal points, and which auto-increment

## NUMBERS WITH DECIMAL POINTS

- these are fully precise but they are less computationally efficient

## `NUMERIC`

- use to store very precise numbers with decimal points like scientific calculations, grams of gold

## `DECIMAL`

## FLOATING POINT MATH NUMERIC TYPES

- use to store numbers with a decimal where decimal is not that important, like kilograms of trash in a landfill, or number of liters in a lake
- floating point math numeric types are much more efficient when it comes to computations

## `REAL`

- full precision is not guaranteed, only about 6 digits of precision is guaranteed

## `DOUBLE PRECISION`

## `FLOAT`

## FAST RULES FOR STORING NUMBERS

![](./images/postgresql/numeric_types_fast_rules.png)

## CHARACTER TYPES

- in PostgresSQL there are no performance differences between these different types unlike in other databases

## `CHAR(x)`

- a string with a fixed (defined) number of characters
- extra chars are trimmed
- unused chars and replaced with space

## `VARCHAR`

- variable length character

## `VARCHAR(40)`

- a string with up to 40 characters, automatically removes extra characters above the limit
- no extra space characters are added like in the `CHAR(x)` type
- this type is mostly used to prevent accidental storing of an extremely long character (which usually is a mistake not an intended behavior)

```sql
VARCHAR(50)
```

## `TEXT`

- stores a string of any length

## BOOLEAN DATA TYPES

Automatic conversion to boolean values:

'true', 'yes', 'on', 1, 't', 'y' => TRUE
'false', 'no', 'off', 0, 'f', 'n' => FALSE
'null' => NULL

```sql
SELECT('yes'::BOOLEAN) -- returns TRUE
```

```sql
SELECT(0::BOOLEAN) -- returns FALSE
```

## `NULL`

- no value, nothing
- not True, not False

```sql
SELECT('null'::BOOLEAN) -- returns `NULL` 
```

## DATE AND TIME VALUES

## DATE CONVERSION

```sql
SELECT ('NOV-20-1980'::DATE); -- converts to 1980-11-20 (YYYY-MM-DD)
```

## TIME CONVERSION (WITH TIME ZONE OR WITHOUT TIME ZONE)

## TIME WITHOUT TIME ZONE

```sql
SELECT ('01:23 PM'::TIME); -- returns 13:23:00
```

## TIME WITH TIME ZONE

- UTC is a base time zone

```sql
SELECT ('01:23:23 AM EST'::TIME WITH TIME ZONE);
-- returns 01:23:23-05:00 
```

## DATETIME (`TIMESTAMP`) WITH TIME ZONE

```sql
SELECT ('NOV-20-1980 1:23 AM PST'::TIMESTAMP WITH TIME ZONE);
```

## AUTOMATIC `TIMESTAMP` ENTRY

```sql
CREATE TABLE users (
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

## INTERVALS

```sql
SELECT ('1 D 2 H 30 M 15 S'::INTERVAL); -- returns '1 day 02:30:15' of type INTERVAL
```

```sql
SELECT ('NOV-11-2022'::DATE) - ('1 D 2 H'::INTERVAL); -- returns '2002-11-09 22:00:00" of type TIMESTAMP WITHOUT TIME ZONE
```

## CALCULATING INTERVALS BETWEEN TIMES OF DIFFERENT TIME ZONES

```sql
SELECT ('NOV-20-1980 1:23 AM EST'::TIMESTAMP WITH TIME ZONE)
- 
SELECT ('NOV-10-1980 5:43 AM PST'::TIMESTAMP WITH ZIME ZONE)
```

## TYPE CONVERSION

Converting a float into an integer

```sql
SELECT (2.0::INTEGER);
```

## OUT OF RANGE ERROR

```sql
SELECT (60000::SMALLINT); -- smallint accepts integer up to range 32767, therefore this will raise error
```

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

## FOREIGN KEY IN POSTGRESQL

- PostgreSQL only allows an entry of a record with a foreign key, if this entry is referencing an existing record in the second table. In order words, it's not possible to enter a new record if this new record is referencing a record which doesn't exist in the second table.

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

## AGGREGATE FUNCTIONS

- aggregate functions takes a range of values and reduces them into a single value
- you can only use aggregate functions on a single field at once
- aggregate functions can't be nested

<https://www.postgresql.org/docs/15/functions-aggregate.html>

- `COUNT()`
- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`

```sql
SELECT MAX(id)
FROM comments;
```

## USING `GROUP BY` AND AGGREGATE FUNCTIONS TOGETHER

```sql
SELECT user_id, MAX(id)
FROM comments
GROUP BY user_id;
```

## `COUNT()`

- `NULL` values don't count in `COUNT()`

In order to count all records, also those including nulls, you `COUNT(*)`

```sql
SELECT COUNT(*) FROM photos;
```

```sql
SELECT user_id, COUNT(*)
FROM comments
GROUP BY user_id;
```

## `HAVING`

- `HAVING` is a filtering clause, similar to `WHERE`.
- `HAVING` always works with `GROUP BY` while `WHERE` works on raw data
- `HAVING` is used to filter set of groups (created by `GROUP BY`)
- most of the time `HAVING` uses an aggregate function as part of it's clause

```sql
SELECT photo_id, COUNT(*)
FROM comments
WHERE photo_id < 3
GROUP BY photo_id
HAVING COUNT(*) > 2;
```

## SORTING USING `ORDER BY`

- sorting is done in ascending order by default, however `ASC` keyword can be used for extra clarity
- sorting works on both numbers and strings

## `ASC` - SORTING BY ASCENDING ORDER (FROM SMALLEST TO LARGEST)

```sql
SELECT *
FROM products
ORDER BY price;
```

## `DESC` - SORTING BY DESCENDING ORDER (FROM LARGEST TO SMALLEST)

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

## DOUBLE SORTING

```sql
SELECT *
FROM products
ORDER BY price, weight DESC;
```

## `OFFSET`

- `OFFSET` is used to skip the first x number of records, where x is defined by `OFFSET`

This query skips first 40 records from the result set.

```sql
SELECT *
FROM users
OFFSET 40;
```

## `LIMIT`

- `LIMIT` is used to limit the number of records to the the number specified by `LIMIT`

The following query skips the first 5 records from the result set

```sql
SELECT *
FROM users
LIMIT 5;
```

## USING `OFFSET` AND `LIMIT` TOGETHER

- they can be used together to display products in an e-commerce shop

Example: when we want to show the first page (first 20 products)

```sql
SELECT *
FROM products
ORDER BY price
LIMIT 20
OFFSET 0;
```

When we want to show the second page of products:

```sql
SELECT *
FROM products
ORDER BY price
LIMIT 20
OFFSET 20;
```

## `UNION`, `INTERSECT` AND `EXCEPT`

- these three clauses are used on queries
- they are used to somehow filter results of two queries (usually on the same table)
- we can only use `UNION`, `INTERSECT` and `EXCEPT` if result sets of queries are the same of the same structure (same field names, and the same data types)

## `UNION`

- `UNION` joins result sets of two queries together
- if results of two queries which are in `UNION` have duplicate records, this record will be included only once
- parentheses around queries are not mandatory but recommended
- we are only allowed to use `UNION` if result sets of queries are the same of the same structure (same field names, and the same data types)

```sql
(
  SELECT * FROM products
	ORDER BY price DESC
	LIMIT 4
)
UNION
(
	SELECT * FROM products
	ORDER BY price / weight DESC
	LIMIT 4
)
```

## `UNION ALL`

- if we don't want to remove duplicates but we want to keep all records, we should use `UNION ALL` instead

```sql
(
  SELECT * FROM products
	ORDER BY price DESC
	LIMIT 4
)
UNION ALL
(
	SELECT * FROM products
	ORDER BY price / weight DESC
	LIMIT 4
)
```

## `INTERSECT`

- `INTERSECT` returns only those records which exist in result sets of both queries

```sql
(
  SELECT * FROM products
	ORDER BY price DESC
	LIMIT 4
)
INTERSECT
(
	SELECT * FROM products
	ORDER BY price / weight DESC
	LIMIT 4
);
```

## `INTERSECT ALL`

- `INTERSECT ALL` returns only those records which exist in result sets of both queries
- if record 1 is present in result set 1 twice and in result set also 2 twice (so four records accross two different result sets), then the `INTERSECT ALL` will return this record twice, or 3 times for 6 records (3 per each result set)

```sql
(
  SELECT * FROM products
	ORDER BY price DESC
	LIMIT 4
)
INTERSECT ALL
(
	SELECT * FROM products
	ORDER BY price / weight DESC
	LIMIT 4
);
```
## `EXCEPT`

- `EXCEPT` will return only those records which are present in the first query and ARE NOT present in the second query
- if there are records which exists in the second query and don't exist in the first query, they will not be returned. For that reason, order of queries matter for the `EXCEPT` clause.

![](./images/postgresql/except.png)

# SUBQUERIES

- subqueries (inner queries) are used to arrive a certain value which will be used as a 'variable' in a secondary query (outer query)
- subquery is returned first
- subquery doesn't require semi-colon at the end of it
- subquery is placed inside the parenthesis

```sql
SELECT name, price -- OUTER QUERY
FROM products
WHERE price > (
  SELECT MAX(price) -- SUBQUERY, INNER QUERY
  FROM products
  WHERE department = 'Toys'
)
```

We can use subqueries in many different locations, which make them challenging to use or understand in other people's code.

```sql
SELECT
  p1.name
  (SELECT COUNT(name) FROM products) -- source of value
FROM (SELECT * FROM products) as p1 -- source of records
JOIN (SELECT * FROM products) as p2 ON p1.id = p2.id -- source of records
WHERE p1.id IN (SELECT id FROM products); -- source of fields
```

In order to use subqueries effectively, it's necessary to understand the shape of the result set of the subquery.

EXAMPLES: SUBQUERY -> SHAPE

1. Full table shape. Both fields and records
2. An array of records. Many records from one field.
3. Scalar value/Scalar query. One record from one field.

Example 1:

```sql
SELECT * FROM orders;
```

![](./images/postgresql/full_shape_subquery.png)

Example 2:

```sql
SELECT id FROM orders;
```

![](./images/postgresql/array_subquery.png)

Example 3:

```sql
SELECT COUNT(*) FROM orders;
```

![](./images/postgresql/scalar_subquery.png)

## SUBQUERIES INSIDE OF A `SELECT` STATEMENT

Array Subquery

```sql
SELECT name, price, (
	SELECT price
	FROM products
  WHERE id = 3
)
FROM products
WHERE price > 867;
```

Scalar Subquery

```sql
SELECT MAX(price) -- returns a field and one value
FROM products
```

## SUBQUERIES INSIDE OF A `FROM` STATEMENT

- subquery of this type has to have an alias applied to it
- any subquery can be used inside the `FROM` statement as long as the result set is compatible with outer `SELECT` and `WHERE` statements. In other words, fields used in `SELECT` and `WHERE` statements must exist in the result set of the subquery

![](./images/postgresql/subquery_inside_from_statement.png)

Example 1

```sql
SELECT name, price_weight_ratio
FROM (
	SELECT name, price / weight AS price_weight_ratio
	FROM products
) AS p
WHERE price_weight_ratio > 5;
```

Example 2

```sql
SELECT *
FROM (SELECT MAX(price) FROM products) AS p;
```

Example 3

```sql
SELECT AVG(p.order_count) -- p. is not mandatory
FROM (
  SELECT user_id, COUNT(*) AS order_count
  FROM orders
  GROUP BY user_id
 ) AS p
 ```

 Example 4

 ```sql
SELECT MAX(p.avg_price) 
FROM (
  SELECT manufacturer, AVG(price) AS avg_price
  FROM phones
  GROUP BY manufacturer
) AS p
 ```

 ## SUBQUERIES IN A `JOIN` CLAUSE

 - any subquery that returns a data set compatible with the `ON` clause

```sql
SELECT first_name
FROM users
JOIN (
	SELECT user_id
	FROM orders
	WHERE product_id = 3
) AS o -- o is an alias for orders
ON o.user_id = users.id;
```

![](./images/postgresql/subquery_inside_join_clause.png)

## SUBQUERIES INSIDE A `WHERE` CLAUSE

- structure of data allowed in the subquery depends on the comparison operator (eg. a single column of records can be used with `IN` operator)
- these types of subqueries are very useful

Example 1

```sql
SELECT id
FROM orders
WHERE product_id IN (
  SELECT id
  FROM products
  WHERE price / weight > 50
);
```

Example 2

```sql
SELECT name, price
FROM products
WHERE price > (
	SELECT AVG(price)
	FROM products
);
```

![](./images/postgresql/data_structures_compatible_with_where_clause.png)

## `NOT IN` OPERATOR WITH A `WHERE` CLAUSE SUBQUERY

```sql
SELECT name, department
FROM products
WHERE department NOT IN (
  SELECT department
  FROM products
  WHERE price < 100
);
```

## `ALL` OPERATOR WITH A `WHERE` CLAUSE SUBQUERY

```sql
SELECT name, department, price
FROM products
WHERE price > ALL (
  SELECT price
  FROM products
  WHERE department = 'Industrial'
);
```

## `SOME` OPERATOR WITH A `WHERE` CLAUSE SUBQUERY

- `SOME` is an alias of `ANY`, they can be used interexchangably

Example

`50 < SOME` vs (20,100) will return True, because 50 is largest than some (or any) of the two values. In this case 50 is greater than 20.

```sql
SELECT name, department, price
FROM products
WHERE price > SOME (
  SELECT price
  FROM products
  WHERE department = 'Industrial'
)
```

## CORRELATED SUBQUERIES

- correlated subqueries are subqueries which use aliases to correlate values between two separate subqueries, in order to make some kind of comparison between records
- correlated subqueries are similar to nested loops, as some value from an outer loop is passed to an inner loop for a comparison
- we can use correlated subqueries inside `SELECT`, `FROM`, `WHERE` and `JOIN`, we can use it everywhere

Example: for each row of the outer query, 'where subquery' will be run 

```sql
SELECT name, department, price
FROM products AS p1 -- alias is necessary, outer query, p1 is passed as a variable to inner query
WHERE p1.price = (
  SELECT MAX(price)
  FROM products AS p2 -- alias is necessary, inner query/subquery
  WHERE p1.department = p2.department
);
```

Example 2: 'select subquery' will be run for every row in the outer query.

```sql
SELECT p1.name, (
  	SELECT COUNT(*)
  	FROM orders AS o1
  	WHERE o1.product_id = p1.id
  ) AS num_orders
FROM products AS p1
```

## USING CORRELATED SUBQUERY TO RUN A 'SELECT QUERY' WIHOUT ANY `FROM` CLAUSE

- in order to achieve this, a subquery have to return a single value (a subquery has to be a scalar subquery)

Example

```sql
SELECT (
	SELECT MAX(price)
  FROM products
);
```

Example 2

```sql
SELECT (
	SELECT MAX(price)
  FROM products
) / (
  SELECT AVG(price)
  FROM products
);
```

Example 3

```sql
SELECT (SELECT MAX(price) FROM phones) AS max_price,
       (SELECT MIN(price) FROM phones) AS min_price,
       (SELECT AVG(price) FROM phones) AS avg_price;
```

## SELECTING `DISTINCT` VALUES

- `DISTINCT` keyword is always placed inside the `SELECT` clause
- `DISTINCT` provides a list of unique values inside a specific field
- useful in the exploratory phase of database analysis


```sql
SELECT DISTINCT department
FROM products;
```

```sql
SELECT COUNT(DISTINCT department)
FROM products;
```

## USING `DISTINCT` TO FIND A LIST OF UNIQUE COMBINATIONS OF RECORD VALUES FROM MULTIPLE FIELDS

- we can't make `COUNT()` in this case

```sql
SELECT DISTINCT department, name
FROM products;
```

## UTILITY OPERATORS

## `GREATEST`

```sql
SELECT GREATEST(200, 10, 30);
```

```sql
SELECT GREATEST(30,
  (SELECT MAX (price * weight) FROM products)
);
```

## `LEAST`

```sql
SELECT LEAST(1000, 20, 50, 100)
```

```sql
SELECT name, price, LEAST (400, price * 0.5)
FROM products;
```

## `CASE KEYWORD`

- if none of the conditions is satisfied, `NULL` is returned

```sql
SELECT name, price,
  CASE
  	WHEN price > 600 THEN 'high'
    WHEN price > 300 THEN 'medium'
    ELSE 'cheap'
  END
 FROM products;
```
## DATABASE-SIDE VALIDATION

## RECORD LEVEL VALIDATION

- is a given value defined at all?
- is provided value unique?
- is provided value larger, smaller, equal, not equal to?

## APPLYING `NOT NULL` CONSTRAINT

- apply during table creation

```sql
CREATE TABLE products (
  price INTEGER NOT NULL
);
```

- after table was created
- if there is already a `NULL` value inside the table, this query will return an error

```sql
ALTER TABLE products
ALTER COLUMN price
SET NOT NULL;
```

## `DEFAULT` COLUMN VALUES

- apply during table creation

```sql
CREATE TABLE products (
  price TIME DEFAULT '00:01 AM'
);
```

- apply after table was created

```sql
ALTER TABLE products
ALTER COLUMN price
SET DEFAULT 9999;
```

## COMBINING A `DEFAULT` AND `NOT NULL` IN ONE CONSTRAINT

- we can combine these two constraints in order to provide an empty string as minimum (when user decides to not add a bio)
- this can be useful for server processing, for example, in Javascript when we run len(x), an empty string would give us value of 0, while `NULL` would raise an error

```sql
CREATE TABLE users (
  bio VARCHAR(400) NOT NULL DEFAULT ''
)
```

## APPLYING A `UNIQUE` CONSTRAINT TO ONE COLUMN

- before table is created

```sql
CREATE TABLE products (
  name VARCHAR(50) UNIQUE
);
```

- applying after table was created
- this constraint can only be added if there are no duplicates in the specified column (all values are already unique)

```sql
ALTER TABLE products
ADD UNIQUE(name);
```

## REMOVING CONSTRAINTS

```sql
ALTER TABLE products
DROP CONSTRAINT products_name_key;
```

## MULTICOLUMN UNIQUENESS

- multi-column uniqueness constraint works over several column
- unique value in the same column is accepted as long as corresponding values in the other column or columns are different, eg. "Shirt, Light Clothes" and "Shirt, Heavy Clothes" are acceptable 

```sql
ALTER TABLE products
ADD UNIQUE (name, department);
```

## CHECK VALIDATION

- before table was created

```sql
CREATE TABLE products (
  price INTEGER CHECK (price > 0)
);
```
- after table was created
- it's only possible to add this check constraint if existing records in the table already pass the constraint
- it's not possible to use subqueries within `CHECK` constraints statements

```sql
ALTER TABLE products
ADD CHECK (price > 0);
```

```sql
CREATE TABLE posts (
  latitude REAL CHECK (latitude IS NULL OR (latitude >= -90 AND latitude <= 90>))
)
```

## CHECK VALIDATION OF MULTIPLE COLUMNS

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  name VARCHAR(40),
  created_at TIMESTAMP NOT NULL,
  est_delivery TIMESTAMP NOT NULL,
  CHECK (created_at < est_delivery)
);
```

## HOW TO CHECK TWO VALUES IN TWO SEPARATE COLUMNS, IF THERE IS ALWAYS A VALUE IN ONE OF THEM, AND NEVER THERE ARE NO VALUES OR TWO VALUES AT THE SAME TIME?

```sql
CHECK
(
  COALESCE((post_id)::BOOLEAN:INTEGER, 0)
  +
  COALESCE((comment_id)::BOOLEAN:INTEGER, 0)
)
```

## WHERE SHOULD WE ADD VALIDATIONS?

WEB SERVER LEVEL
- most of the validation rules, non-critical ones should be applied at the web server level
- easier to express more complex validations
- far easier to apply new validation rules
- many libraries handle validations automatically

DATABASE LEVEL
- critical validation rules should be applied at the database level
- validation still apply even if you connect from a different client
- guaranteed that validation is always applied
- can only apply new validation rules if all existing rows satisfy it

## DATABASE STRUCTURE DESIGN PATTERNS

1. Polymorphic association
2. Separate column for each 'reaction' type
3. Separate table for each 'reaction' type

Disclaimer: 'reaction' here refers to a reaction type on a social media post (likes, loves, sads). These patterns were considered as possible solutions to implement a reaction system in a social media site.

## POLYMORPHIC ASSOCIATIONS

- they are not recommended to use, but they are used in practice quite often
- it's a situation where a column in one table refers to more than one table, but the reference is not enforced using foreign and private keys
- in this case, the task of figuring out to which referenced tables, the base table is referring to is outside of SQL (mearning is deciphered by server or client)
- IMPORTANT: foreign key can't be used in polymorphic association
- polymorphic association results in data consistency (and for that reason is not recommended)

## RATIONALE FOR CHOOSIGN DIFFERENT DESIGNS

1. When deciding whether to go for a solution with one table and extra columns or two tables, it's important to consider whether rate of query for each table is going to be different. If so, it is advisable to go for two tables solution because performance efforts can be applied to one table only. The one requiring it.

2. Another important consideration is expectation of future changes to any of the tables (due to change or further development of features). If you think it's likely that at least one of the tables can be modified in the future (by adding extra column), it is advisable to go for two tables solution. In this solution it is possible to change only one table. Doing this has two benefits: the second functionality will not be affected. Second, it's also about segregation of responsibilities. One program should be responsible for one behavior only.

## DERIVED DATA

- derived data is data which is not stored separately in a table, instead is calculated/queried on demand, it's derived from other existing data
- eg. number of followers is derived from followers table, the total number itself is not stored separately

## `COALESCE` FUNCTION

- `COALESCE` looks at the values which are provided as arguments and it returns the first value which is not `NULL`

```sql
SELECT COALESCE(NULL, 5); -- returns 5
```

```sql
SELECT COALESCE(NULL, 5, 8); -- returns 5
```

```sql
SELECT COALESCE(10, 5); -- returns 10
```

## USING `COALESCE` TO TURN DIFFERENT NUMERIC VALUES INTO ZERO OR ONE

```sql
SELECT COALESCE((post_id)::BOOLEAN:INTEGER, 0)'
```

## ADVANCED TOPICS

## `SHOW` KEYWORD

- `SHOW` shows a particular piece of Postgres configuration

## `SHOW data_directory`

- show where Postrgres stores data on the local machine

```sql
SHOW data_directory; -- C:/Program Files/PostgreSQL/15/data
```

## HOW TO GET A LIST OF DATABASE NAMES WITH CORRESPONDING IDENTIFIERS (`OID`)?

```sql
SELECT oid, datname
FROM pg_database;
```

## HOW TO GET A LIST OF ALL FILES STORED ON A LOCAL MACHINES WITH CORRESPONDING IDENTIFIERS (`OID`)?

```sql
SELECT * FROM pg_class;
```

## HOW IS DATA STORED IN POSTRESQL?

HEAP/HEAP FILE

- a file that contains all the data (rows) of a particular table
- heap data structure is not the same as heap file
- each heap file consists of several blocks
- 'users' table (OID: 17002) is a heap file

BLOCK/PAGE

- a heap file is divided into many different blocks or pages. Each page/block stores some number of rows
- each block consists of several different tuples/items
- each block is 8kb in size

![](./images/postgresql/block_structure.png)

![](./images/postgresql/block_binary.png)

TUPLE/ITEM

- individual row from the table

![](./images/postgresql/heap_block_tuple.png)

## PERFORMANCE

- FULL TABLE SCAN - every time Postgresql loads records from hard drive to RAM, it has a relatively high performance cost
- items in an index structure are stored ordered (numerical order for numbers, alphabetical order for strings)

## INDEX - HOW IT'S STRUCTURED AND HOW IT WORKS

- Index is a data structure that efficiently tells us what block/item a record is stored at 
- most common index is a B-Tree index

![](./images/postgresql/index_structure.png)

## CREATING AN INDEX

- if you don't specify a name for an index, a name will be assigned automatically (eg. in the following example, the name of the index will be `users_username_idx`)

```sql
CREATE INDEX ON users(username); -- users is the name a table and username is a name of a column
```

```sql
CREATE INDEX users_username_idx ON users(username);
```

## DELETING AN INDEX

```sql
DROP INDEX users_username_idx;
```

## BENCHMARKING

- running the same query on indexed vs unindexed records can improve performance 10x
- the following query was tested, and performance without index was 0.50ms, and performance with index was 0.05ms

```sql
EXPLAIN ANALYZE SELECT * FROM users
WHERE username = 'Emil30'
```

## DOWNSIDES OF INDICES

- creating indices increases storage space and this can be very costly on large databases stored on cloud servers (or even locally, as it will require more harddrives, machines and DevOps engineers)
- indices slow down `INSERT/UPDATE/DELETE` operations because indices have to be updated after every single one of these operations
- users may not use an index alltogether

## GET SIZE OF A COLUMN

```sql
SELECT pg_size_pretty(pg_relation_size('users'));
```

## INDEX TYPES

- B-TREE INDEX - standard index, used 99% of the time, described in the section above

- HASH - speeds up simple equality checks

- GiST - geometry, full text search

- SP-GiST - clustered data, such as dates - many rows might have the same year

- GIN - for columns that contain arrays or JSON data

- BRIN - specialized for really large datasets

## AUTOMATICALLY GENERED INDICES

- PostrgreSQL automatically creates an index for the primary key column of every table, `column_name_pkey`
- PostgresSQL automatically creates an index for any `UNIQUE` constrained column, `column_name2_key`
- these indices don't get listed in the PGAdmin

## SHOW ALL INDICES (INCLUDING HIDDEN)

```sql
SELECT relname, relkind
FROM pg_class
WHERE relkind = 'i';
```

## POSTGRES EXTENSIONS

- extensions are out-of-the-box applications which gives us extra functionalities in PostrgreSQL

## `pageinspect` EXTENSION

```sql
CREATE EXTENSIONS pageinspect;
```

## DISPLAY INFORMATION ABOUT A PARTICULAR INDEX (B-TREE)

```sql
SELECT *
FROM bt_metap('users_username-idx')
```

- `bt` stands for B-Tree
- `metap` stands for meta page 

## `CTID`

```sql
SELECT ctid, *
FROM users
WHERE username = 'aali'; 
```

`CTID` is an identifier inside of an index. It has two separate storage conventions for two separate data types. 
- if stored data is a row (tuple), then `ctid` points out to where a particular row is stored within a block
- ctid is hidden unless specifically required by a query

(1,0) - page 1, 

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

## KEYBOARD SHORTCUTS

- `CTRL + /` - comment/uncomment a single or multiple lines

<https://www.pgadmin.org/docs/pgadmin4/6.18/keyboard_shortcuts.html>

## SQL SCHEMA DESIGNERS

- configuration file-like diagraming

<https://dbdiagram.io>

- manual diagraming

<https://ondras.zarovi.cz/sql/demo>

## ISSUE WITH SLOW POSTGRESQL ON WINDOWS 10

In my `C:\Program Files\PostgreSQL\14\data\postgresql.conf` file I found `listen_addresses = "*"` which I changed to `listen_addresses = 'localhost'`.

<https://dba.stackexchange.com/questions/201646/slow-connect-time-to-postgresql-on-windows-10>

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

## TOPICS TO REPEAT AND DO MORE EXERCISES

- `UNION`
- `INTERSECT`
- `EXCEPT`