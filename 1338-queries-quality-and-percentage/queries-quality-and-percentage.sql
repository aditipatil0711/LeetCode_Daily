/* Write your T-SQL query statement below */
SELECT query_name, ROUND(SUM(rating*1.0/position)/count(*),2) as quality,
ROUND(SUM(case WHEN rating <3 then 1 else 0 end )*100.0/ COUNT(*),2)  as poor_query_percentage 
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name
