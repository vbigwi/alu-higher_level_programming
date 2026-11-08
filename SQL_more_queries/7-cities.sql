-- Creates the database hbtn_0d_usa and its table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table cities referencing the states table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
