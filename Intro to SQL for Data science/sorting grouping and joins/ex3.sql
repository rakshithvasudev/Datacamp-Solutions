SELECT title
FROM films 
WHERE release_year IN (2000,2012)
ORDER BY release_year;

SELECT *
FROM films 
WHERE release_year NOT IN (2015)
ORDER BY duration;

SELECT title, gross
FROM films 
WHERE title LIKE 'M%'
ORDER BY title;