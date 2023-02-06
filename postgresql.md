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

## ALIASING

```sql
SELECT name AS first_name, year_hired
FROM employees;
```

`name` is a name of a field in a table, while `first_name` will be a name of the field in the result set

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

## Collation

Collation specifies how data is sorted and compared in a database. Collation provides the sorting rules, case and accent sensitivity properties for the data in the database.

For example, when you run a query using the `ORDER BY` clause, collation determines whether or not uppercase letters and lowercase letters are treated the same.

## SERIAL

`SERIAL` in PostgresSQL lets you create an auto-increment column. By default, it creates values of type integer. It is a good practice to use auto-increments for primary keys.

## PRIMARY KEY

`PRIMARY KEY` is a constraint which enforces the column values to be non-null and unique. It lets you uniquely identify a specific set of instanced present in the table.

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

`Employee` table stores employee records. `Address` table stores adresses of employees. Each employee will have only one record in the `Employee` table but it can have zero, one or several records in `Address` table. This is because each employee can have zero, one or several addresses (Home address, Office address, Vacations address).

![](./images/postgresql/one-to-many2.png)

`Employee` table and `Address` table are linked by the key column `EmployeeID`'. `EmployeeId` is a primary key in `Employee` table and a foreign key in `Address` table.

![](./images/postgresql/one-to-many.png)

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