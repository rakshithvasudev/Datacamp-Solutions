/*
Simple filtering of text
Remember, the WHERE clause can also be used to filter text results, such as names or countries.

For example, this query gets the titles of all films which were filmed in China:

SELECT title
FROM films
WHERE country = 'China';
Now it's your turn to practice using WHERE with text values!

Important: in PostgreSQL (the version of SQL we're using), you must use single quotes with WHERE.

*/

Select name,birthdate from people 
where birthdate='1974-11-11' 

Select Count(*) from films 
where language='Hindi' 

Select * from films 
where certification='R' 
