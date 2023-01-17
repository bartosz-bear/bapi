# PostgreSQL

<https://www.datacamp.com/tutorial/beginners-introduction-postgresql>

## Syntax

Keywords are not case-sensitive in SQL, but data is.

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

Database schema is the organization and structure of a database. A schema contains schema objects, which could be tables, columns, data types, views, stored procedures, relationships, primary keys, foreign keys, etc.

![](./images/postgresql/database_schema.png)