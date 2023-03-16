--  a script that lists all the cities of California 
-- that can be found in the database hbtn_0d_usa
-- states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command


USE hbtn_0d_usa;
SELECT name
FROM states 
WHERE name = 'California';
ORDER BY cities.id ASC;
