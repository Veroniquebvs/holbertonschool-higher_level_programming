-- script that creates the database hbtn_0d_usa 
-- and the table cities (in the database hbtn_0d_usa)

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
)