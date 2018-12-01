SELECT COUNT(*) FROM (SELECT release_year, COUNT(*)
FROM films
GROUP BY release_year
HAVING COUNT(*)>200) AS result;