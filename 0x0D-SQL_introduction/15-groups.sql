-- This script will lists the number of records with the same score
-- A query that will list the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
