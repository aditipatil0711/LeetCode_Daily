/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT Email,
    ROW_NUMBER() OVER (PARTITION BY Email ORDER BY Id) AS Num
    FROM Person 
)
DELETE FROM CTE WHERE Num > 1
 
