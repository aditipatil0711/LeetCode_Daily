# Write your MySQL query statement below
SELECT person_name FROM 
(
SELECT *,SUM(weight) OVER(ORDER BY turn) as TotalWeight from Queue) as T
WHERE TotalWeight<=1000
ORDER BY TotalWeight DESC
LIMIT 1

