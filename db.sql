-- Implementing a 1 : 1 relationship
Drop Database if exists datarep;
Create Database datarep default CHARACTER SET = utf8 default COLLATE = utf8_general_ci;
Use datarep;
-- Documentation 13.1.17.3 version 5.6
-- Section 14.5.6  version 5.6

-- The parent and child tables must use the same storage engine
-- Foreign key columns and Primary key column must be exactly the same

-- RESTRICT Rejects the delete or update operation for the parent table
Create Table Blogposts
(
	id Int(8) unsigned auto_increment,
    name varchar(30),
	blogtext varchar(255) not null,
	Primary key (id)
) engine = INNODB;