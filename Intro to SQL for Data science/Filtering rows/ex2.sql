/*
Simple filtering of numeric values
As you learned in the previous exercise, the WHERE clause can also be used to filter numeric records, such as years or ages.

For example, the following query selects all details for films with a budget over ten thousand dollars:

SELECT *
FROM films
WHERE budget > 10000;
Now it's your turn to use the WHERE clause to filter numeric values!

INSTRUCTIONS 1/3
35 XP
1
Get all details for all films released in 2016.

Take Hint (-10 XP)
2
Get the number of films released before 2000.

3
Get the title and release year of films released after 2000.
*/

SELECT * from films
where release_year='2016'

SELECT title, release_year from films
where release_year>2000
