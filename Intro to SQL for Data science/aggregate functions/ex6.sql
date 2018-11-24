-- get the count(deathdate) and multiply by 100.0
-- then divide by count(*)

SELECT  (COUNT(deathdate)*100.0/COUNT(*)) AS percentage_dead
FROM people;


SELECT MAX(release_year)-MIN(release_year) AS difference
FROM films;



SELECT (MAX(release_year)-MIN(release_year))/10 AS number_of_decades
FROM films;