SELECT title, gross-budget AS net_profit
FROM films;

SELECT title, duration/60.0 AS duration_hours
FROM films;

SELECT AVG(duration)/60.0 AS avg_duration_hours
FROM films;