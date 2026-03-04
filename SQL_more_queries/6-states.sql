-- script that creates the database hbtn_0d_usa 
-- and the table states (in the database hbtn_0d_usa)

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
)