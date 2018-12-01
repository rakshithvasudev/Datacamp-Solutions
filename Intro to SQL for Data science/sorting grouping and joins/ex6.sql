SELECT release_year, COUNT(*)
FROM films 
GROUP BY release_year;


SELECT release_year, AVG(duration)
FROM films 
GROUP BY release_year;

SELECT release_year, MAX(budget)
FROM films 
GROUP BY release_year;


SELECT imdb_score, COUNT(*)
FROM reviews 
GROUP BY imdb_score;