/*All together now
Time to practice using ORDER BY, GROUP BY and HAVING together.

Now you're going to write a query that returns the average budget and average gross earnings for films in each year after 1990, if the average budget is greater than $60 million.

This is going to be a big query, but you can handle it!
*/

SELECT release_year,budget,gross
FROM films;

SELECT release_year,budget,gross
FROM films
WHERE release_year >1990;

SELECT release_year
FROM films
WHERE release_year >1990
GROUP BY release_year;

SELECT release_year, AVG(budget) AS avg_budget ,AVG(gross) AS avg_gross
FROM films
WHERE release_year >1990
GROUP BY release_year;

SELECT release_year, AVG(budget) AS avg_budget ,AVG(gross) AS avg_gross
FROM films
WHERE release_year >1990
GROUP BY release_year
HAVING AVG(budget)>60000000;

SELECT release_year, AVG(budget) AS avg_budget ,AVG(gross) AS avg_gross
FROM films
WHERE release_year >1990
GROUP BY release_year
HAVING AVG(budget)>60000000
ORDER BY avg_gross DESC;


