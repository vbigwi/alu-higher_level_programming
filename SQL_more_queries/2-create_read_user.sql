-- Creates the database hbtn_0d_2 and a read-only user user_0d_2 on it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user if it does not exist yet
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Gives only the SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
