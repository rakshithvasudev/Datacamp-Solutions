/*
WHERE IN
As you've seen, WHERE is very useful for filtering results. However, if you want to filter based on many conditions, WHERE can get unwieldy. For example:

SELECT name
FROM kids
WHERE age = 2
OR age = 4
OR age = 6
OR age = 8
OR age = 10;
Enter the IN operator! The IN operator allows you to specify multiple values in a WHERE clause, making it easier and quicker to specify multiple OR conditions! Neat, right?

So, the above example would become simply:

SELECT name
FROM kids
WHERE age IN (2, 4, 6, 8, 10);
Try using the IN operator yourself!
*/

select title, release_year 
from films
where (release_year = 1990 or release_year = 2000)
and duration > 120

select title, language 
from films
where language IN ('English','Spanish','French');

select title, language 
from films
where certification IN ('NC-17','R');
