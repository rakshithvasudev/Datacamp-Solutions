-- select country, average budget, average gross
SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
-- from the films table
FROM films 
-- group by country 
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(*)>10
-- order by country
ORDER BY COUNTRY
-- limit to only show 5 results
LIMIT 5