/*
BETWEEN (2)
Similar to the WHERE clause, the BETWEEN clause can be used with multiple AND and OR operators, so you can build up your queries and make them even more powerful!

For example, suppose we have a table called kids. We can get the names of all kids between the ages of 2 and 12 from the United States:

SELECT name
FROM kids
WHERE age BETWEEN 2 AND 12
AND nationality = 'USA';
Take a go at using BETWEEN with AND on the films data to get the title and release year of all Spanish language films released between 1990 and 2000 (inclusive) with budgets over $100 million. We have broken the problem into smaller steps so that you can build the query as you go along!

INSTRUCTIONS 1/4
25 XP
1
2
3
4
Get the title and release year of all films released between 1990 and 2000 (inclusive).
*/

SELECT title, release_year
FROM films
WHERE release_year
BETWEEN 1990 AND 2000;

SELECT title, release_year
FROM films
WHERE release_year
BETWEEN 1990 AND 2000
AND budget > 100000000;

SELECT title, release_year
FROM films
WHERE release_year
BETWEEN 1990 AND 2000
AND budget > 100000000
AND language='Spanish';

SELECT title, release_year
FROM films
WHERE release_year
BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language='Spanish' or language='French');

