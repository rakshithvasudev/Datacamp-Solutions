/*
SELECT name
FROM companies
WHERE name LIKE 'DataC_mp';
You can also use the NOT LIKE operator to find records that don't match the pattern you specify.

Got it? Let's practice!

INSTRUCTIONS 1/3
35 XP
1
Get the names of all people whose names begin with 'B'. The pattern you need is 'B%'.

Take Hint (-10 XP)
2
Get the names of people whose names have 'r' as the second letter. The pattern you need is '_r%'.

3
Get the names of people whose names don't start with A. The pattern you need is 'A%'.
*/

select name 
from people 
where name like 'B%' 

select name 
from people 
where name like '_r%' 

select name 
from people 
where name not like 'A%' 