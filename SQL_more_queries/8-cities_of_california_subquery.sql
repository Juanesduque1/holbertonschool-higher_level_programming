-- Script that lists all the cities found in a databse
SELECT 'id', 'name' FROM cities
WHERE 'state_id' = (
    SELECT 'id' FROM states WHERE 'name' = 'California'
)
ORDER BY cities.'id' ASC;
