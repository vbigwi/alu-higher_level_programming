-- Creates the database hbtn_0d_usa and its table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table states with an auto generated primary key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
