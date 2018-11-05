/*
WHERE AND OR (2)
You now know how to select rows that meet some but not all conditions by combining AND and OR.

For example, the following query selects all films that were released in 1994 or 1995 which had a rating of PG or R.

SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');
Now you'll write a query to get the title and release year of films released in the 90s which were in French or Spanish and which took in more than $2M gross.

It looks like a lot, but you can build the query up one step at a time to get comfortable with the underlying concept in each step. Let's go!

INSTRUCTIONS 1/3
35 XP
1
2
3
Get the title and release year for films released in the 90s.
*/

select title, release_year 
from film,
where release_year >= 1990 and release_year < 2000;

select title, release_year 
from films
where (release_year >= 1990 and release_year < 2000)
and (language='French' or language='Spanish');

select title, release_year 
from films
where (release_year >= 1990 and release_year < 2000)
and (language='French' or language='Spanish')
and gross>2000000;