-- Script that creates a table with unique value
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE, 
    name VARCHAR(256)
);
