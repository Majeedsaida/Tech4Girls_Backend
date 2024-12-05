# SQL Database Scripts for Tech4Girls
This repository contains SQL scripts to set up a basic database for Tech4Girls_DB, including tables for users, posts, and courses.
SQL (Structured Query Language) is a specialized programming language designed for managing and manipulating relational databases. It provides a standardized way to interact with databases by allowing users to create, read, update, and delete data—commonly referred to as CRUD operations.
![](https://dbconvert.com/blog/content/images/2024/05/sql-chatgpt44.jpg)

1. Setting Up and Populating a Database question1.sql
Description:
This script creates the Tech4Girls_DB database and a Users table, and it inserts sample data for three users.

Key SQL Concepts:
Creating a database.
Creating a table with PRIMARY KEY, AUTO_INCREMENT, and TIMESTAMP.
Inserting sample data into a table.

2. Building Relationships question2.sql
Description:
This script creates a Posts table and establishes a one-to-many relationship between the Users and Posts tables using a foreign key.

Key SQL Concepts:
Creating a table with a foreign key.
Defining a one-to-many relationship between tables.

3. Creating Many-to-Many Relationships question3.sql
Description:
This script sets up a Courses table and an intermediate User_Courses table to form a many-to-many relationship between Users and Courses.

Key SQL Concepts:
Creating an intermediate table for a many-to-many relationship.
Using composite primary keys and foreign keys to link tables.

## Author
* Abdul-Majeed Saidatu

## Installation
```bash
first, fork this repository and
git clone https://github.com/Majeedsaida/Tech4Girls_Backend.git

```
## Tech Stack
* python
* SQL
