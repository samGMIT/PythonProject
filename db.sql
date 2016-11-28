-- Implementing a 1 : 1 relationship
Drop Database if exists datarep;
Create Database datarep default CHARACTER SET = utf8 default COLLATE = utf8_general_ci;
Use datarep;
-- Documentation 13.1.17.3 version 5.6
-- Section 14.5.6  version 5.6

-- The parent and child tables must use the same storage engine
-- Foreign key columns and Primary key column must be exactly the same

-- RESTRICT Rejects the delete or update operation for the parent table
Create Table Orders
(
	id Int(8) unsigned auto_increment,
    items varchar(252) not null,
	price Float(10) not null,
	Primary key (id)
) engine = INNODB;

Create Table Bookings
(
    id Int(8) unsigned auto_increment,
	numPeople Int(2) not null,
    orderDate date not null,
    bookedDate date not null,
    phoneNr Int(12) not null,
    name varchar(64) not null,
    Primary key (id)
) engine = INNODB;