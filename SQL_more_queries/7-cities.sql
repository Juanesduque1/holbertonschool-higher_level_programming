-- Script that creates a database and a table
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'cities' (
    'id' INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    'state_id' INT NOT NULL,
    'name' VARCHAR(256) NOT NULL
    FOREIGN KEY ('state_id') REFERENCES hbtn_0d_usa.states ('id')
);
